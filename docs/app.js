/* Renders window.DATA (results, params, tables) into the page. */
(function () {
  const D = window.DATA || {};
  const R = D.results || { scenarios: [], opportunities: [], unit_economics: [] };
  const RT = D.results_typical || R;
  const P = D.params || {};
  const T = D.tables || {};
  const fmt = window.viz.fmt;
  const $ = id => document.getElementById(id);

  function h(tag, cls, parent, text) {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  function money(v, d = 0) { return v == null ? "n/a" : (v < 0 ? "-$" : "$") + Math.abs(v).toLocaleString(undefined, { maximumFractionDigits: d, minimumFractionDigits: d }); }
  function num(v, d = 0) { return v == null ? "n/a" : (+v).toLocaleString(undefined, { maximumFractionDigits: d }); }
  function pct(v) { return v == null ? "n/a" : Math.round(v * 100) + "%"; }
  function big(v) { if (v == null) return "n/a"; if (v >= 1e12) return (v / 1e12).toFixed(1) + "T"; if (v >= 1e9) return (v / 1e9).toFixed(0) + "B"; if (v >= 1e6) return (v / 1e6).toFixed(0) + "M"; return num(v); }
  function cell(v, kind) {
    if (v === null || v === undefined || v === "") return "n/a";
    if (kind === "money") return money(v);
    if (kind === "money2") return money(v, 2);
    if (kind === "pct") return pct(v);
    if (kind === "big") return big(v);
    if (kind === "bool") return v === true ? "yes" : v === false ? "no" : String(v);
    if (kind === "num") return num(v, 2);
    return String(v);
  }

  /* Generic sortable table. cols: [{k, l, kind, w}] */
  function table(container, rows, cols, opts = {}) {
    if (typeof container === "string") container = $(container);
    if (!container) return;
    container.innerHTML = "";
    if (!rows || !rows.length) { h("p", "small", container, opts.empty || "No data in this table yet."); return; }
    const wrap = h("div", "tablewrap", container);
    const tbl = h("table", null, wrap);
    const thead = h("thead", null, tbl), tr = h("tr", null, thead);
    let sortKey = opts.sort || null, sortDir = opts.dir || -1;
    cols.forEach(c => {
      const th = h("th", c.kind && c.kind !== "text" && c.kind !== "bool" && c.kind !== "tag" ? "num" : null, tr, c.l);
      th.style.cursor = "pointer"; th.title = "Sort";
      th.onclick = () => { if (sortKey === c.k) sortDir = -sortDir; else { sortKey = c.k; sortDir = (c.kind === "text" ? 1 : -1); } draw(); };
    });
    const tb = h("tbody", null, tbl);
    function draw() {
      tb.innerHTML = "";
      let rs = rows.slice();
      if (sortKey) rs.sort((a, b) => { const x = a[sortKey], y = b[sortKey]; if (x == null) return 1; if (y == null) return -1; return (x < y ? -1 : x > y ? 1 : 0) * sortDir; });
      if (opts.limit) rs = rs.slice(0, opts.limit);
      rs.forEach(r => {
        const trr = h("tr", opts.hl && opts.hl(r) ? "hl" : null, tb);
        cols.forEach(c => {
          const td = h("td", c.kind && c.kind !== "text" && c.kind !== "bool" && c.kind !== "tag" ? "num" : null, trr);
          if (c.kind === "tag") { const v = r[c.k]; const sp = h("span", "tag " + (c.tagClass ? c.tagClass(v) : ""), td, v == null ? "n/a" : String(v)); }
          else if (c.kind === "link") { if (r[c.k]) { const a = h("a", null, td, c.l === "Source" ? "source" : r[c.k]); a.href = r[c.k]; a.target = "_blank"; a.rel = "noopener"; } else td.textContent = "n/a"; }
          else td.textContent = c.f ? c.f(r) : cell(r[c.k], c.kind);
          if (r.est && c.k === cols[0].k) h("span", "tag est", td, "est").style.marginLeft = "6px";
        });
      });
    }
    draw();
    if (opts.note) h("p", "src", container, opts.note);
  }
  const tagYesNo = v => v === "yes" || v === true ? "ok" : v === "no" || v === false ? "no" : v === "crypto" ? "crypto" : "gray";

  /* ---------- derived: cheapest permissive source per GPU (from params) */
  function gpuRates() {
    return (P.gpus || []).map(g => {
      const r = g.rates || {};
      const get = k => (r[k] && r[k].value != null) ? r[k].value : null;
      const prov = k => (r[k] && (r[k].provider || r[k].source)) || "";
      return { gpu: g.key, label: g.label, ondemand: get("ondemand"), m1: get("m1"), m3: get("m3"), m12: get("m12"), test: get("test_rate"), vast: g.vast_median_rent && g.vast_median_rent.value, prov_m1: prov("m1"), prov_m12: prov("m12"), prov_test: prov("test_rate"), est_m3: !!(r.m3 && /estimate/i.test(r.m3.source || "")), est_m12: !!(r.m12 && /estimate|ceiling/i.test(r.m12.source || "")) };
    });
  }

  /* ---------- hero */
  function hero() {
    const el = $("hero-stats"); if (!el) return;
    const sc = R.scenarios || [];
    const pick = (plan, s, name) => sc.find(x => x.plan === plan && x.budget === s && x.scenario.startsWith(name));
    const c2b = pick("C", 100000, "2b"), a2b = pick("A", 100000, "2b"), c1 = pick("C", 100000, "1.");
    const tiles = [];
    if (c2b) tiles.push({ k: "Best plan, $100k prepaid 12 mo, 40% util", v: money(c2b.by_util[1].after_tax_12mo), d: "after-tax 12-month result, 8x B200 node, thin-host models (conservative throughput)", cls: c2b.by_util[1].after_tax_12mo >= 0 ? "pos" : "neg" });
    if (c2b) tiles.push({ k: "2026 tax saved on a $100k December prepay", v: money(c2b.by_util[1].tax_saved_2026), d: "49.3% of the net 2026 loss, within the $256k cap", cls: "pos" });
    if (a2b) tiles.push({ k: "Original idea (single H100s, gpt-oss and Llama)", v: money(a2b.by_util[1].after_tax_12mo), d: "after-tax 12-month result at 40% util, $100k prepaid; small token pools, 10 to 21 providers", cls: "neg" });
    if (c1) tiles.push({ k: "Cash at risk, month-to-month test", v: money(c1.cash_at_risk), d: "one month of a $100k-per-year plan; cancel any time", cls: "" });
    tiles.forEach(t => { const s = h("div", "stat", el); h("div", "k", s, t.k); h("div", "v " + t.cls, s, t.v); h("div", "d", s, t.d); });
  }

  /* ---------- A. supply */
  function supply() {
    const rows = gpuRates();
    table("tbl-rates", rows, [
      { k: "label", l: "GPU", kind: "text" },
      { k: "m1", l: "Month-to-month $/GPU-hr", kind: "money2" },
      { k: "prov_m1", l: "Source", kind: "text" },
      { k: "test", l: "Single-GPU test rate", kind: "money2" },
      { k: "prov_test", l: "Test source", kind: "text" },
      { k: "m3", l: "3-month", kind: "money2", f: r => money(r.m3, 2) + (r.est_m3 ? " (est)" : "") },
      { k: "m12", l: "12-month", kind: "money2", f: r => money(r.m12, 2) + (r.est_m12 ? " (est)" : "") },
      { k: "vast", l: "Vast median (renter pays)", kind: "money2" },
    ], { note: "Rates are the cheapest source whose terms permit (or do not forbid) a public paid API. Vultr 8-GPU plans need a manually reviewed account, so the test rate is a single-GPU source (Koyeb, Lambda, DigitalOcean). Full sources in data/params.json." });
    const s = T.supply || [];
    table("tbl-supply", s, [
      { k: "provider", l: "Provider", kind: "text" },
      { k: "h100_od", l: "H100 SXM", kind: "money2" }, { k: "h200_od", l: "H200", kind: "money2" }, { k: "b200_od", l: "B200", kind: "money2" },
      { k: "mi300x_od", l: "MI300X", kind: "money2" }, { k: "mi355x_od", l: "MI355X", kind: "money2" }, { k: "rtxpro6000_od", l: "RTX PRO 6000", kind: "money2" },
      { k: "a100_od", l: "A100", kind: "money2" }, { k: "l40s_od", l: "L40S", kind: "money2" }, { k: "rtx4090_od", l: "4090", kind: "money2" }, { k: "rtx5090_od", l: "5090", kind: "money2" },
      { k: "m12", l: "12-month", kind: "text" }, { k: "min_unit", l: "Min unit", kind: "text" }, { k: "start", l: "Start", kind: "text" },
      { k: "api_allowed", l: "Paid API allowed", kind: "tag", tagClass: tagYesNo },
      { k: "src", l: "Source", kind: "link" },
    ], { sort: "h100_od", dir: 1, note: "On-demand USD per GPU-hour, read 2026-10-22. Blank cells: not offered or not published. 'silent' means the terms neither permit nor forbid a paid API; 'ambiguous' means supplemental terms could not be read." });
    table("tbl-tos", s.filter(r => r.tos_quote), [
      { k: "provider", l: "Provider", kind: "text" },
      { k: "api_allowed", l: "Verdict", kind: "tag", tagClass: tagYesNo },
      { k: "tos_quote", l: "Clause (verbatim)", kind: "text" },
      { k: "tos_url", l: "Terms", kind: "link" },
    ], { sort: "provider", dir: 1 });
    table("tbl-nodes", T.node_prices || [], [
      { k: "node", l: "Node", kind: "text" }, { k: "provider", l: "Provider", kind: "text" }, { k: "node_hourly", l: "$/node-hr", kind: "money2" }, { k: "per_gpu", l: "$/GPU-hr", kind: "money2" }, { k: "term", l: "Term", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ], { sort: "per_gpu", dir: 1 });
  }

  /* ---------- B. demand */
  function demand() {
    table("tbl-marketplaces", T.marketplaces || [], [
      { k: "name", l: "Marketplace", kind: "text" },
      { k: "accepts_outside_providers", l: "Accepts outside providers", kind: "tag", tagClass: v => v === "yes" ? "ok" : v === "crypto" ? "crypto" : v === "no" ? "no" : "gray" },
      { k: "how_to_join", l: "How to join", kind: "text" }, { k: "approval_time", l: "Approval", kind: "text" },
      { k: "requirements", l: "Requirements", kind: "text" }, { k: "payment", l: "Payment", kind: "text" }, { k: "fees", l: "Fees", kind: "text" },
      { k: "traffic_evidence", l: "Traffic evidence", kind: "text" }, { k: "small_provider_traffic", l: "Small providers", kind: "text" },
      { k: "src", l: "Source", kind: "link" },
    ]);
    const om = (T.openrouter_models || []).map(r => ({ ...r, per_provider: r.weekly_tokens && r.providers ? r.weekly_tokens / r.providers : null }));
    table("tbl-ormodels", om, [
      { k: "slug", l: "Model", kind: "text" }, { k: "providers", l: "Providers", kind: "num", f: r => num(r.providers) },
      { k: "min_in", l: "Min in $/M", kind: "num" }, { k: "median_in", l: "Median in", kind: "num" }, { k: "min_out", l: "Min out $/M", kind: "num" }, { k: "median_out", l: "Median out", kind: "num" },
      { k: "weekly_tokens", l: "Tokens/week", kind: "big" }, { k: "per_provider", l: "Tokens/week per provider", kind: "big" }, { k: "notes", l: "Notes", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ], { sort: "weekly_tokens", dir: -1, note: "Prices in USD per million tokens from OpenRouter's public endpoints API, 2026-10-22. Free endpoints and disabled endpoints excluded." });
    // chart: tokens per provider, top 15
    const top = om.filter(r => r.per_provider).sort((a, b) => b.per_provider - a.per_provider).slice(0, 15);
    const c = $("chart-openings"); if (c && top.length) {
      h("h4", "ct", c, "Weekly OpenRouter tokens per provider (the opening metric)");
      window.viz.groupedBars(c, { categories: top.map(r => r.slug.split("/")[1] + " (" + r.providers + ")"), series: [{ name: "Tokens per week per provider", values: top.map(r => r.per_provider / 1e9) }], kind: "num", labelWidth: 230, labels: true, note: "Billions of tokens per week divided by provider count. Number in parentheses = providers. Source: openrouter.ai rankings and endpoints API, 2026-10-22." });
    }
  }

  /* ---------- C. resale */
  function resale() {
    table("tbl-resale", T.resale || [], [
      { k: "name", l: "Marketplace", kind: "text" }, { k: "host_requirements", l: "Host requirements", kind: "text" },
      { k: "owns_hardware_required", l: "Must own hardware", kind: "bool" }, { k: "vm_allowed", l: "VM / rented allowed", kind: "text" },
      { k: "fee_or_share", l: "Fee or share", kind: "text" }, { k: "payout", l: "Payout", kind: "text" },
      { k: "renter_price_h100", l: "H100 renter price", kind: "text" }, { k: "renter_price_4090", l: "4090", kind: "text" }, { k: "renter_price_5090", l: "5090", kind: "text" },
      { k: "crypto", l: "Crypto", kind: "bool" }, { k: "verdict", l: "Verdict", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ]);
    table("tbl-spread", T.spread || [], [
      { k: "gpu", l: "GPU", kind: "text" }, { k: "rent_cost_hr", l: "Rent cost $/hr", kind: "money2" }, { k: "vast_median_hr", l: "Vast median $/hr", kind: "money2" }, { k: "host_share", l: "Host share", kind: "text" }, { k: "host_take_hr", l: "Host take $/hr", kind: "money2" }, { k: "spread_hr", l: "Spread $/hr at 100%", kind: "money2" }, { k: "breakeven_util", l: "Breakeven util", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ], { note: "Estimates. Vast's implied host share is about 80% (Vast blog: live prices are about 25% above what hosts earn). Vast's hosting agreement requires the host to be the sole owner of the hardware, and every rental contract read bans resale, so this route only works with owned hardware." });
  }

  /* ---------- D. unit economics */
  function unitEconomics() {
    const opp = R.opportunities || [], oppT = RT.opportunities || [];
    const gpus = [...new Set(opp.map(o => o.gpu))];
    const sel = $("sel-gpu"); if (!sel) return;
    gpus.forEach(g => { const o = h("option", null, sel, g); o.value = g; });
    sel.value = gpus.includes("B200") ? "B200" : gpus[0];
    const tSel = $("sel-case");
    function draw() {
      const g = sel.value;
      const rows = opp.filter(o => o.gpu === g).sort((a, b) => b.rev_per_gpu_hour_100 - a.rev_per_gpu_hour_100);
      const typ = Object.fromEntries(oppT.filter(o => o.gpu === g).map(o => [o.model, o]));
      const c = $("chart-rev"); c.innerHTML = "";
      h("h4", "ct", c, `Revenue per GPU-hour at 100% utilization vs rental cost, ${g}`);
      window.viz.groupedBars(c, {
        categories: rows.map(r => r.model.split("/")[1]),
        series: [
          { name: "Revenue, conservative throughput", values: rows.map(r => r.rev_per_gpu_hour_100) },
          { name: "Revenue, typical throughput", values: rows.map(r => (typ[r.model] || {}).rev_per_gpu_hour_100 || null) },
          { name: "Rental cost (month-to-month)", values: rows.map(r => r.cost_m1), color: "var(--muted)" },
        ], kind: "money2", labelWidth: 200, rowHeight: 50,
        note: "Priced 5% under today's OpenRouter floor, 3 prompt tokens per completion token, 20% prefill haircut. A model earns money only when the revenue bar is longer than the cost bar at a utilization you can reach."
      });
      const c2 = $("chart-breakeven"); c2.innerHTML = "";
      h("h4", "ct", c2, `Utilization needed to break even on month-to-month rent, ${g}`);
      const be = rows.filter(r => r.breakeven_util_m1 != null).map(r => ({ m: r.model.split("/")[1], v: Math.min(r.breakeven_util_m1, 3) }));
      window.viz.groupedBars(c2, { categories: be.map(r => r.m), series: [{ name: "Breakeven utilization (conservative)", values: be.map(r => r.v) }], kind: "pct", labelWidth: 200, labels: true, highlight: (c, s, v) => v <= 0.7, note: "Bars over 100% mean the model cannot pay for the GPU even when fully busy. Values are capped at 300% for display. Dimmed bars need more than 70% utilization." });
      table("tbl-opp", rows.map(r => ({ ...r, model_short: r.model, rev_typ: (typ[r.model] || {}).rev_per_gpu_hour_100 })), [
        { k: "model_short", l: "Model", kind: "text" }, { k: "gpus_per_replica", l: "GPUs/replica", kind: "num", f: r => num(r.gpus_per_replica) },
        { k: "tps_out_per_gpu", l: "Output tok/s per GPU", kind: "num", f: r => num(r.tps_out_per_gpu) },
        { k: "price_out_new", l: "Your price out $/M", kind: "num", f: r => num(r.price_out_new, 3) }, { k: "price_in_new", l: "Your price in $/M", kind: "num", f: r => num(r.price_in_new, 3) },
        { k: "rev_per_gpu_hour_100", l: "Rev/GPU-hr @100% (cons.)", kind: "money2" }, { k: "rev_typ", l: "@100% (typical)", kind: "money2" },
        { k: "cost_m1", l: "Rent $/hr", kind: "money2" }, { k: "breakeven_util_m1", l: "Breakeven util", kind: "pct" },
        { k: "providers", l: "Providers", kind: "num", f: r => num(r.providers) }, { k: "weekly_tokens", l: "Tokens/wk", kind: "big" },
        { k: "gpus_supported_at_70pct", l: "GPUs the demand supports @70%", kind: "num", f: r => r.gpus_supported_at_70pct == null ? "n/a" : num(r.gpus_supported_at_70pct, 1) },
        { k: "capturable_rev_week", l: "Capturable rev/wk", kind: "money" },
      ], { sort: "rev_per_gpu_hour_100", dir: -1, note: "Capturable demand assumes a new cheapest provider wins at most 7% of a model's OpenRouter tokens (observed: floor-priced gpt-oss-120b endpoints carried 0.8% and 7.2% of a day's tokens). Estimates." });
    }
    sel.onchange = draw; draw();
    table("tbl-throughput", T.throughput || [], [
      { k: "model", l: "Model", kind: "text" }, { k: "gpu", l: "GPU", kind: "text" }, { k: "gpus_per_replica", l: "GPUs/replica", kind: "num", f: r => num(r.gpus_per_replica) },
      { k: "tps_out_conservative", l: "Output tok/s per GPU, conservative", kind: "num", f: r => num(r.tps_out_conservative) }, { k: "tps_out_typical", l: "Typical", kind: "num", f: r => num(r.tps_out_typical) },
      { k: "source_type", l: "Basis", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ], { sort: "model", dir: 1 });
  }

  /* ---------- E. scenarios */
  function scenarios() {
    const sc = R.scenarios || [], scT = RT.scenarios || [];
    const plans = [...new Map(sc.map(s => [s.plan, s.plan_label])).entries()];
    const selP = $("sel-plan"), selS = $("sel-spend"), selU = $("sel-util"), selC = $("sel-case");
    plans.forEach(([k, l]) => { const o = h("option", null, selP, l); o.value = k; });
    selP.value = plans.some(p => p[0] === "C") ? "C" : plans[0][0];
    [50000, 100000, 250000].forEach(s => { const o = h("option", null, selS, money(s)); o.value = s; });
    selS.value = 100000;
    [0.2, 0.4, 0.7].forEach(u => { const o = h("option", null, selU, pct(u)); o.value = u; });
    selU.value = 0.4;
    function draw() {
      const plan = selP.value, S = +selS.value, u = +selU.value, useT = selC.value === "typical";
      const src = useT ? scT : sc;
      const rows = src.filter(s => s.plan === plan && s.budget === S);
      const ui = [0.2, 0.4, 0.7].indexOf(u);
      const pl = (P.plans || []).find(p => p.key === plan) || {};
      $("plan-desc").textContent = `${pl.label || plan}. Models: ${(pl.models || []).join(", ")}. Node size ${pl.node_size || 1}.`;
      const flat = rows.map(s => { const b = s.by_util[ui]; return {
        scenario: s.scenario, blocked: s.blocked_for_rented, gpus: s.gpus, node_months: s.node_months_affordable, rate: s.rate_per_gpu_hour, monthly_cost: s.monthly_cost,
        rev_month: b.rev_month, profit_month: b.profit_month, rev_2026: b.rev_2026, ded: b.deductible_2026 != null ? b.deductible_2026 : b.deductible_2026_fed, ded_ca: b.deductible_2026_ca,
        tax: b.tax_saved_2026, cash: s.cash_at_risk, after: b.after_tax_12mo != null ? b.after_tax_12mo : b.after_tax_12mo_cash, pre: b.profit_12mo_pretax != null ? b.profit_12mo_pretax : b.profit_12mo_pretax_cash, exit: s.exit, lock: s.lock_in, block_reason: s.block_reason }; });
      table("tbl-scenarios", flat, [
        { k: "scenario", l: "Scenario", kind: "text", f: r => r.scenario + (r.blocked ? " (blocked for rented GPUs)" : "") },
        { k: "gpus", l: "GPUs", kind: "num", f: r => num(r.gpus, 1) }, { k: "rate", l: "$/GPU-hr", kind: "money2" },
        { k: "monthly_cost", l: "Cost/month", kind: "money" }, { k: "rev_month", l: "Revenue/month", kind: "money" }, { k: "profit_month", l: "Profit/month", kind: "money" },
        { k: "ded", l: "Deductible 2026", kind: "money" }, { k: "tax", l: "Tax saved 2026", kind: "money" }, { k: "cash", l: "Cash at risk", kind: "money" },
        { k: "pre", l: "12-mo pre-tax", kind: "money" }, { k: "after", l: "12-mo after tax", kind: "money" },
        { k: "lock", l: "Lock-in", kind: "text" }, { k: "exit", l: "Exit", kind: "text" },
      ], { hl: r => r.scenario.startsWith("6a") || r.scenario.startsWith("6b"), note: "Budget = 12-month spend at the term's rate (owned: capital). 2026 revenue counts hours from Dec 1 (staged: from Nov 15). Tax saved = 37% federal + 12.3% CA of the net 2026 loss, capped at $256k federal and $313k CA. Scenarios 3a, 3b and 5 are shown for comparison only: Vast requires hosts to own their hardware. Highlighted rows are the staged test-then-prepay path." });
      const c = $("chart-after"); c.innerHTML = "";
      h("h4", "ct", c, `12-month after-tax result by scenario, ${money(S)} budget, ${useT ? "typical" : "conservative"} throughput`);
      const ok = rows.filter(s => !s.blocked_for_rented);
      window.viz.groupedBars(c, { categories: ok.map(s => s.scenario.replace(/^\S+\s/, "").slice(0, 46)), series: [0, 1, 2].map(i => ({ name: pct([0.2, 0.4, 0.7][i]) + " utilization", values: ok.map(s => { const b = s.by_util[i]; return b.after_tax_12mo != null ? b.after_tax_12mo : b.after_tax_12mo_cash; }) })), kind: "money", labelWidth: 290, rowHeight: 56, note: "Revenue for 12 months minus 12 months of cost (or the purchase price for owned hardware), plus the 2026 tax saved." });
      const c2 = $("chart-tax"); c2.innerHTML = "";
      h("h4", "ct", c2, `2026 deduction and tax saved by scenario, ${money(S)} budget, ${pct(u)} utilization`);
      window.viz.groupedBars(c2, { categories: ok.map(s => s.scenario.replace(/^\S+\s/, "").slice(0, 46)), series: [{ name: "Deductible in 2026", values: ok.map(s => { const b = s.by_util[ui]; return b.deductible_2026 != null ? b.deductible_2026 : b.deductible_2026_fed; }) }, { name: "Tax saved in 2026", values: ok.map(s => s.by_util[ui].tax_saved_2026) }], kind: "money", labelWidth: 290, rowHeight: 40, note: "Owned hardware: federal deduction shown (100% bonus); California allows only $25k Section 179 plus 5% MACRS in year one." });
    }
    [selP, selS, selU, selC].forEach(s => s.onchange = draw); draw();
    // plan comparison chart at $100k, 40%
    const c3 = $("chart-plans"); if (c3) {
      const rows = sc.filter(s => s.budget === 100000 && (s.scenario.startsWith("1.") || s.scenario.startsWith("2b") || s.scenario.startsWith("4.")));
      const short = l => l.replace(/^Plan /, "").split(",")[0].replace(" (Vultr)", "");
      const cats = [...new Set(rows.map(r => short(r.plan_label)))];
      const ser = ["1.", "2b", "4."].map(pfx => ({ name: pfx === "1." ? "Month-to-month" : pfx === "2b" ? "12-month prepaid" : "Owned (capital)", values: cats.map(cn => { const r = rows.find(x => short(x.plan_label) === cn && x.scenario.startsWith(pfx)); return r ? r.by_util[1].after_tax_12mo != null ? r.by_util[1].after_tax_12mo : r.by_util[1].after_tax_12mo_cash : null; }) }));
      h("h4", "ct", c3, "Plans compared: 12-month after-tax result, $100k budget, 40% utilization, conservative throughput");
      window.viz.groupedBars(c3, { categories: cats, series: ser, kind: "money", labelWidth: 230, rowHeight: 52, note: "Only the B200 and MI355X node plans serving the thin-host, list-priced models come close to paying for themselves. Single-GPU plans on commodity models lose money at any term." });
    }
  }

  /* ---------- F. tax */
  function tax() {
    table("tbl-tax", T.tax || [], [
      { k: "topic", l: "Topic", kind: "text" }, { k: "rule", l: "Rule", kind: "text" }, { k: "citation", l: "Citation", kind: "text" }, { k: "quote", l: "Quote", kind: "text" }, { k: "how_it_applies", l: "How it applies", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ]);
    table("tbl-licenses", T.licenses || [], [
      { k: "model", l: "Model", kind: "text" }, { k: "license", l: "License", kind: "text" }, { k: "commercial_api_ok", l: "Paid API OK", kind: "bool" }, { k: "attribution_or_limits", l: "Limits", kind: "text" }, { k: "quote", l: "Quote", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ]);
    table("tbl-privacy", T.privacy || [], [{ k: "topic", l: "Topic", kind: "text" }, { k: "requirement", l: "Requirement", kind: "text" }, { k: "src", l: "Source", kind: "link" }]);
    // prepay calculator
    const amt = $("calc-amt"), rev = $("calc-rev"), other = $("calc-other"), out = $("calc-out");
    if (!amt) return;
    const tx = P.tax || {};
    const fed = (tx.fed_rate || {}).value || 0.37, ca = (tx.ca_rate || {}).value || 0.123, capF = (tx.excess_business_loss_cap || {}).value || 256000, capC = (tx.ca_excess_business_loss_cap || {}).value || 313000;
    function calc() {
      const a = +amt.value || 0, r = +rev.value || 0, o = +other.value || 0;
      const loss = Math.max(0, a - r);
      const roomF = Math.max(0, capF - o), roomC = Math.max(0, capC - o);
      const usedF = Math.min(loss, roomF), usedC = Math.min(loss, roomC);
      const saved = usedF * fed + usedC * ca;
      const carry = Math.max(0, loss - roomF);
      out.innerHTML = `<div class="grid">
        <div class="stat"><div class="k">Net 2026 business loss</div><div class="v">${money(loss)}</div><div class="d">prepay minus December revenue</div></div>
        <div class="stat"><div class="k">2026 tax saved</div><div class="v pos">${money(saved)}</div><div class="d">${pct(fed)} federal on ${money(usedF)} + ${pct(ca)} CA on ${money(usedC)}</div></div>
        <div class="stat"><div class="k">After-tax cost of the prepay</div><div class="v">${money(a - saved)}</div><div class="d">what the 12 months of GPU time really costs you</div></div>
        <div class="stat"><div class="k">Carried forward (over federal cap)</div><div class="v">${money(carry)}</div><div class="d">becomes an NOL for 2027+</div></div></div>`;
    }
    [amt, rev, other].forEach(i => i.oninput = calc); calc();
  }

  /* ---------- alternatives */
  function alternatives() {
    table("tbl-alt", T.alternatives || [], [
      { k: "accelerator", l: "Accelerator", kind: "text" }, { k: "memory_gb", l: "GB", kind: "num", f: r => num(r.memory_gb) }, { k: "cheapest_hr", l: "Cheapest $/hr", kind: "money2" }, { k: "cheapest_source", l: "Source", kind: "text" }, { k: "min_unit", l: "Min unit", kind: "text" }, { k: "start", l: "Start", kind: "text" },
      { k: "tps_gptoss120b", l: "gpt-oss-120b tok/s (InferenceX, total)", kind: "num", f: r => num(r.tps_gptoss120b) }, { k: "tps_deepseek_r1", l: "DeepSeek R1 tok/s", kind: "num", f: r => num(r.tps_deepseek_r1) },
      { k: "tokens_per_dollar_vs_h100", l: "Tokens per $ vs H100", kind: "num" }, { k: "maturity_note", l: "Notes", kind: "text" }, { k: "api_allowed", l: "Paid API", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ], { sort: "tokens_per_dollar_vs_h100", dir: -1, note: "InferenceX per-GPU throughput counts prompt plus output tokens on its 8k/1k workload; output-only is about one ninth of the listed figure." });
    table("tbl-macs", T.macs || [], [
      { k: "machine", l: "Machine", kind: "text" }, { k: "price", l: "Price", kind: "money" }, { k: "memory_gb", l: "GB", kind: "num", f: r => num(r.memory_gb) }, { k: "bandwidth_gbs", l: "GB/s", kind: "num", f: r => num(r.bandwidth_gbs) },
      { k: "tps_gptoss120b_single", l: "gpt-oss-120b tok/s (1 user)", kind: "num" }, { k: "tps_gptoss120b_batch", l: "batched", kind: "num" }, { k: "tps_deepseek_batch", l: "DeepSeek batched", kind: "num" }, { k: "prefill_tps", l: "Prefill tok/s", kind: "num" }, { k: "ttft_note", l: "TTFT", kind: "text" },
      { k: "cost_per_m_output_gptoss", l: "$/M output gpt-oss", kind: "num" }, { k: "cost_per_m_output_deepseek", l: "$/M output DeepSeek", kind: "num" }, { k: "hosted_option", l: "Hosted", kind: "text" }, { k: "verdict", l: "Verdict", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ]);
    table("tbl-buy", T.owned_hardware || [], [
      { k: "item", l: "Item", kind: "text" }, { k: "price", l: "Price", kind: "money" }, { k: "stock_text", l: "Stock (verbatim)", kind: "text" }, { k: "seller", l: "Seller", kind: "text" }, { k: "lead_time", l: "Lead time", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ]);
    table("tbl-colo", T.colo || [], [
      { k: "provider", l: "Provider", kind: "text" }, { k: "location", l: "Location", kind: "text" }, { k: "offer", l: "Offer", kind: "text" }, { k: "price_month", l: "$/month", kind: "text" }, { k: "cents_kwh", l: "c/kWh", kind: "text" }, { k: "power_kw", l: "kW", kind: "text" }, { k: "setup", l: "Setup", kind: "text" }, { k: "remote_hands", l: "Remote hands", kind: "text" }, { k: "min_term", l: "Min term", kind: "text" }, { k: "accepts_shipped", l: "Accepts shipped gear", kind: "bool" }, { k: "src", l: "Source", kind: "link" },
    ]);
    table("tbl-crypto", T.crypto || [], [
      { k: "network", l: "Network", kind: "text" }, { k: "pays_in", l: "Pays in", kind: "text" }, { k: "usd_per_gpu_day_4090", l: "$/day 4090", kind: "num" }, { k: "usd_per_gpu_day_5090", l: "$/day 5090", kind: "num" }, { k: "usd_per_gpu_day_h100", l: "$/day H100", kind: "num" }, { k: "usd_per_node_day_8xh200", l: "$/day 8x H200", kind: "num" },
      { k: "rented_allowed", l: "Rented GPUs allowed", kind: "text" }, { k: "net_61_days_rented_4090", l: "Net Nov-Dec, rented 4090", kind: "text" }, { k: "net_61_days_owned_4090", l: "owned 4090", kind: "text" }, { k: "net_61_days_owned_h100", l: "owned H100", kind: "text" }, { k: "verdict", l: "Verdict", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ]);
    table("tbl-routes", T.other_routes || [], [
      { k: "realism_rank", l: "#", kind: "num", f: r => num(r.realism_rank) }, { k: "route", l: "Route", kind: "text" }, { k: "what", l: "What", kind: "text" }, { k: "join", l: "Join", kind: "text" }, { k: "requirements", l: "Requirements", kind: "text" }, { k: "payment", l: "Payment", kind: "text" }, { k: "fees", l: "Fees", kind: "text" }, { k: "evidence", l: "Evidence", kind: "text" }, { k: "time_to_first_dollar", l: "First dollar", kind: "text" }, { k: "rented_ok", l: "Rented OK", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ], { sort: "realism_rank", dir: 1 });
    table("tbl-niche", T.niche || [], [
      { k: "model", l: "Model", kind: "text" }, { k: "weekly_tokens", l: "Tokens/wk", kind: "big" }, { k: "providers", l: "Providers", kind: "num", f: r => num(r.providers) }, { k: "min_out", l: "Min out $/M", kind: "num" }, { k: "median_out", l: "Median out", kind: "num" }, { k: "who_serves", l: "Who serves", kind: "text" }, { k: "license", l: "License", kind: "text" }, { k: "content_risk", l: "Content risk", kind: "text" }, { k: "opening_note", l: "Opening", kind: "text" }, { k: "src", l: "Source", kind: "link" },
    ], { sort: "weekly_tokens", dir: -1 });
    table("tbl-modalities", T.modalities || [], [{ k: "modality", l: "Modality", kind: "text" }, { k: "marketplace", l: "Marketplace", kind: "text" }, { k: "outside_provider_ok", l: "Outside providers", kind: "text" }, { k: "unit_price", l: "Unit price", kind: "text" }, { k: "src", l: "Source", kind: "link" }]);
    table("tbl-niche-risks", T.niche_risks || [], [{ k: "risk", l: "Risk", kind: "text" }, { k: "detail", l: "Detail", kind: "text" }, { k: "src", l: "Source", kind: "link" }]);
    // price trend chart
    const pt = (T.price_trend || []).filter(r => r.price != null && r.date);
    const c = $("chart-trend");
    if (c && pt.length) {
      const h100 = pt.filter(r => /H100/i.test(r.gpu)).sort((a, b) => a.date.localeCompare(b.date));
      const h200 = pt.filter(r => /H200/i.test(r.gpu)).sort((a, b) => a.date.localeCompare(b.date));
      const dates = [...new Set([...h100, ...h200].map(r => r.date))].sort();
      const at = (arr, d) => { const r = arr.find(x => x.date === d); return r ? r.price : null; };
      h("h4", "ct", c, "Rental price per GPU-hour over time (published indices and trackers)");
      window.viz.lines(c, { x: dates, series: [{ name: "H100", values: dates.map(d => at(h100, d)) }, { name: "H200", values: dates.map(d => at(h200, d)) }], kind: "money2", note: "Points are different sources (SemiAnalysis composite, Ornn, Silicon Data, GetDeploying medians, provider list prices), so the line mixes methodologies. 2026 prices rose after HBM supply tightened." });
      table("tbl-trend", pt, [{ k: "date", l: "Date", kind: "text" }, { k: "gpu", l: "GPU", kind: "text" }, { k: "price", l: "$/GPU-hr", kind: "money2" }, { k: "source_name", l: "Source", kind: "text" }, { k: "src", l: "Link", kind: "link" }], { sort: "date", dir: 1 });
    }
    table("tbl-forecast", T.forecast || [], [{ k: "source", l: "Source", kind: "text" }, { k: "forecast_text", l: "Forecast", kind: "text" }, { k: "src", l: "Link", kind: "link" }]);
  }

  function sources() {
    const el = $("sources"); if (!el) return;
    const s = T.sources || [];
    const ul = h("ul", "small", el);
    s.forEach(x => { const li = h("li", null, ul); const a = h("a", null, li, x.title || x.url); a.href = x.url; a.target = "_blank"; a.rel = "noopener"; });
  }

  document.addEventListener("DOMContentLoaded", () => {
    hero(); supply(); demand(); resale(); unitEconomics(); scenarios(); tax(); alternatives(); sources();
  });
})();
