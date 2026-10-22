/* Minimal SVG chart helpers. No dependencies.
   Each chart renders into a container and adds a "Table" toggle twin.
   Colors come from CSS custom properties on .viz-root. */
(function () {
  const NS = "http://www.w3.org/2000/svg";
  const SERIES = ["--series-1", "--series-2", "--series-3", "--series-4", "--series-5", "--series-6", "--series-7", "--series-8"];

  function el(tag, attrs, parent) {
    const e = document.createElementNS(NS, tag);
    for (const k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function h(tag, cls, parent, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  function fmt(v, kind) {
    if (v == null || isNaN(v)) return "n/a";
    if (kind === "money") return (v < 0 ? "-$" : "$") + Math.abs(v).toLocaleString(undefined, { maximumFractionDigits: 0 });
    if (kind === "money2") return (v < 0 ? "-$" : "$") + Math.abs(v).toFixed(2);
    if (kind === "pct") return Math.round(v * 100) + "%";
    if (kind === "int") return Math.round(v).toLocaleString();
    return (+v).toLocaleString(undefined, { maximumFractionDigits: 2 });
  }
  function niceTicks(min, max, n) {
    if (min === max) { max = min + 1; }
    const span = max - min, step0 = span / n, mag = Math.pow(10, Math.floor(Math.log10(step0)));
    const cand = [1, 2, 2.5, 5, 10].map(m => m * mag);
    const step = cand.find(s => span / s <= n) || cand[cand.length - 1];
    const lo = Math.floor(min / step) * step, hi = Math.ceil(max / step) * step;
    const ticks = [];
    for (let t = lo; t <= hi + 1e-9; t += step) ticks.push(+t.toFixed(10));
    return { lo, hi, ticks };
  }
  function tooltip() {
    let t = document.getElementById("viz-tip");
    if (!t) { t = h("div", "viz-tip", document.body); t.id = "viz-tip"; }
    return t;
  }
  function showTip(evt, html) {
    const t = tooltip(); t.innerHTML = html; t.style.display = "block";
    const pad = 12, w = t.offsetWidth, hgt = t.offsetHeight;
    let x = evt.clientX + pad, y = evt.clientY + pad;
    if (x + w > window.innerWidth - 8) x = evt.clientX - w - pad;
    if (y + hgt > window.innerHeight - 8) y = evt.clientY - hgt - pad;
    t.style.left = (x + window.scrollX) + "px"; t.style.top = (y + window.scrollY) + "px";
  }
  function hideTip() { const t = tooltip(); t.style.display = "none"; }

  function tableTwin(container, header, rows) {
    const wrap = h("div", "viz-table", container);
    const tbl = h("table", null, wrap);
    const thead = h("thead", null, tbl), trh = h("tr", null, thead);
    header.forEach(x => h("th", null, trh, x));
    const tb = h("tbody", null, tbl);
    rows.forEach(r => { const tr = h("tr", null, tb); r.forEach((c, i) => h("td", i ? "num" : null, tr, c)); });
    wrap.style.display = "none";
    return wrap;
  }
  function toggle(container, svgWrap, tbl) {
    const bar = h("div", "viz-toggle", container);
    const b1 = h("button", "on", bar, "Chart"), b2 = h("button", null, bar, "Table");
    b1.onclick = () => { svgWrap.style.display = ""; tbl.style.display = "none"; b1.className = "on"; b2.className = ""; };
    b2.onclick = () => { svgWrap.style.display = "none"; tbl.style.display = ""; b2.className = "on"; b1.className = ""; };
    container.insertBefore(bar, container.firstChild);
  }

  /* Grouped horizontal bars.
     opts: { categories:[...], series:[{name, values:[...]}], kind:"money"|..., title, note, highlight:(cat,series,value)=>bool, zeroLine:true, colorIndex:[...] } */
  function groupedBars(container, opts) {
    container.classList.add("viz-root");
    const cats = opts.categories, series = opts.series, kind = opts.kind || "num";
    const W = Math.max(560, container.clientWidth || 720), labelW = opts.labelWidth || 200, right = 60;
    const rowH = opts.rowHeight || (series.length > 1 ? 14 * series.length + 14 : 28), top = 10, bottom = 40;
    const H = top + rowH * cats.length + bottom;
    const svgWrap = h("div", "viz-svg", container);
    const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, width: "100%", role: "img", "aria-label": opts.title || "chart" }, svgWrap);
    const all = series.flatMap(s => s.values).filter(v => v != null);
    const minV = Math.min(0, ...all), maxV = Math.max(0, ...all);
    const { lo, hi, ticks } = niceTicks(minV, maxV, 5);
    const x0 = labelW, x1 = W - right;
    const xs = v => x0 + (v - lo) / (hi - lo) * (x1 - x0);
    ticks.forEach(t => {
      el("line", { x1: xs(t), x2: xs(t), y1: top, y2: H - bottom, class: "grid" }, svg);
      const tx = el("text", { x: xs(t), y: H - bottom + 16, class: "tick", "text-anchor": "middle" }, svg);
      tx.textContent = fmt(t, kind === "money2" ? "money" : kind);
    });
    if (lo < 0) el("line", { x1: xs(0), x2: xs(0), y1: top, y2: H - bottom, class: "axis" }, svg);
    const bh = Math.max(6, (rowH - 8) / series.length - 2);
    cats.forEach((c, i) => {
      const y = top + i * rowH;
      const lab = el("text", { x: x0 - 8, y: y + rowH / 2 + 4, class: "label", "text-anchor": "end" }, svg);
      lab.textContent = c;
      series.forEach((s, j) => {
        const v = s.values[i]; if (v == null) return;
        const yy = y + 4 + j * (bh + 2);
        const left = Math.min(xs(0), xs(v)), wdt = Math.abs(xs(v) - xs(0));
        const col = s.color || `var(${SERIES[(opts.colorIndex ? opts.colorIndex[j] : j) % 8]})`;
        const hl = opts.highlight ? opts.highlight(c, s.name, v) : true;
        const r = el("rect", { x: left, y: yy, width: Math.max(wdt, 1), height: bh, rx: 3, fill: col, opacity: hl ? 1 : 0.35 }, svg);
        r.addEventListener("mousemove", e => showTip(e, `<b>${c}</b><br>${s.name}: ${fmt(v, kind)}`));
        r.addEventListener("mouseleave", hideTip);
        if (opts.labels) {
          const t = el("text", { x: v >= 0 ? xs(v) + 4 : left - 4, y: yy + bh - 1, class: "val", "text-anchor": v >= 0 ? "start" : "end" }, svg);
          t.textContent = fmt(v, kind);
        }
      });
    });
    if (series.length > 1) {
      const lg = h("div", "viz-legend", container);
      series.forEach((s, j) => {
        const it = h("span", "lg", lg); const sw = h("i", null, it);
        sw.style.background = s.color || `var(${SERIES[(opts.colorIndex ? opts.colorIndex[j] : j) % 8]})`; h("span", null, it, s.name);
      });
    }
    const tbl = tableTwin(container, ["", ...series.map(s => s.name)], cats.map((c, i) => [c, ...series.map(s => fmt(s.values[i], kind))]));
    toggle(container, svgWrap, tbl);
    if (opts.note) h("p", "viz-note", container, opts.note);
  }

  /* Line chart. opts: { x:[labels], series:[{name, values}], kind, title, note } */
  function lines(container, opts) {
    container.classList.add("viz-root");
    const xl = opts.x, series = opts.series, kind = opts.kind || "num";
    const W = Math.max(560, container.clientWidth || 720), H = opts.height || 300;
    const left = 64, right = 24, top = 16, bottom = 36;
    const svgWrap = h("div", "viz-svg", container);
    const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, width: "100%", role: "img", "aria-label": opts.title || "chart" }, svgWrap);
    const all = series.flatMap(s => s.values).filter(v => v != null);
    const { lo, hi, ticks } = niceTicks(Math.min(0, ...all), Math.max(...all), 5);
    const xs = i => left + i / Math.max(1, xl.length - 1) * (W - left - right);
    const ys = v => top + (hi - v) / (hi - lo) * (H - top - bottom);
    ticks.forEach(t => {
      el("line", { x1: left, x2: W - right, y1: ys(t), y2: ys(t), class: t === 0 ? "axis" : "grid" }, svg);
      const tx = el("text", { x: left - 8, y: ys(t) + 4, class: "tick", "text-anchor": "end" }, svg); tx.textContent = fmt(t, kind === "money2" ? "money" : kind);
    });
    const every = Math.ceil(xl.length / 8);
    xl.forEach((l, i) => { if (i % every === 0 || i === xl.length - 1) { const t = el("text", { x: xs(i), y: H - bottom + 18, class: "tick", "text-anchor": "middle" }, svg); t.textContent = l; } });
    series.forEach((s, j) => {
      const col = s.color || `var(${SERIES[j % 8]})`;
      const d = s.values.map((v, i) => (v == null ? "" : (i === 0 || s.values[i - 1] == null ? "M" : "L") + xs(i) + " " + ys(v))).join(" ");
      el("path", { d, fill: "none", stroke: col, "stroke-width": 2, "stroke-linejoin": "round", "stroke-dasharray": s.dash || "" }, svg);
      const last = s.values.length - 1;
      const lab = el("text", { x: xs(last) - 4, y: ys(s.values[last]) - 6, class: "val", "text-anchor": "end" }, svg); lab.textContent = s.name;
    });
    const cross = el("line", { x1: 0, x2: 0, y1: top, y2: H - bottom, class: "axis", style: "display:none" }, svg);
    const hit = el("rect", { x: left, y: top, width: W - left - right, height: H - top - bottom, fill: "transparent" }, svg);
    hit.addEventListener("mousemove", e => {
      const pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY; const p = pt.matrixTransform(svg.getScreenCTM().inverse());
      const i = Math.max(0, Math.min(xl.length - 1, Math.round((p.x - left) / (W - left - right) * (xl.length - 1))));
      cross.setAttribute("x1", xs(i)); cross.setAttribute("x2", xs(i)); cross.style.display = "";
      showTip(e, `<b>${xl[i]}</b><br>` + series.map(s => `${s.name}: ${fmt(s.values[i], kind)}`).join("<br>"));
    });
    hit.addEventListener("mouseleave", () => { cross.style.display = "none"; hideTip(); });
    const lg = h("div", "viz-legend", container);
    series.forEach((s, j) => { const it = h("span", "lg", lg); const sw = h("i", null, it); sw.style.background = s.color || `var(${SERIES[j % 8]})`; h("span", null, it, s.name); });
    const tbl = tableTwin(container, ["", ...series.map(s => s.name)], xl.map((l, i) => [l, ...series.map(s => fmt(s.values[i], kind))]));
    toggle(container, svgWrap, tbl);
    if (opts.note) h("p", "viz-note", container, opts.note);
  }

  window.viz = { groupedBars, lines, fmt };
})();
