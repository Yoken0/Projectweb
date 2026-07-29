const takeaways = [
  "Stability",
  "AI",
  "Flexibility",
  "Self advocacy",
  "Connection",
  "Transparency",
  "Opportunity",
];

const emerging = [
  "Fears + concerns",
  "Resources",
  "Toolkit",
  "Connection + networking",
];

const leaders = [
  "Emerging talent",
  "Intern management",
  "Team connection",
  "AI as a tool",
  "HR transparency",
];

export default function Home() {
  return (
    <main>
      <header className="topbar">
        <a className="brand" href="#top" aria-label="Back to top">
          CAPSTONE<span>●</span>
        </a>
        <nav aria-label="Primary navigation">
          <a href="#overview">Overview</a>
          <a href="#timeline">Timeline</a>
          <a href="#pathways">Pathways</a>
        </nav>
        <span className="edition">01—07</span>
      </header>

      <section className="hero" id="top">
        <div className="hero-noise" />
        <div className="orbit orbit-one" />
        <div className="orbit orbit-two" />
        <p className="eyebrow">Website outline / Everyone</p>
        <h1>
          <span className="line line-one">THE</span>
          <span className="line line-two">NEXT</span>
          <span className="line line-three">CHAPTER</span>
        </h1>
        <a className="scroll-cue" href="#overview">
          <span>Enter outline</span>
          <i aria-hidden="true">↓</i>
        </a>
        <div className="hero-stamp" aria-hidden="true">
          <span>3</span>
          <span>6</span>
          <span>12</span>
        </div>
      </section>

      <div className="ticker" aria-hidden="true">
        <div>
          EXECUTIVE SUMMARY <b>✦</b> PRESENTATION <b>✦</b> KEY TAKEAWAYS{" "}
          <b>✦</b> ACTION PLAN <b>✦</b> EXECUTIVE SUMMARY <b>✦</b>{" "}
          PRESENTATION <b>✦</b> KEY TAKEAWAYS <b>✦</b> ACTION PLAN <b>✦</b>
        </div>
      </div>

      <section className="overview section" id="overview">
        <div className="section-index">01 / Overview</div>
        <div className="overview-grid">
          <article className="outline-card summary-card">
            <span>01</span>
            <h2>Executive<br />Summary</h2>
            <div className="card-arrow">↗</div>
          </article>
          <article className="outline-card presentation-card">
            <span>02</span>
            <div className="play-mark" aria-hidden="true">▶</div>
            <h2>Presentation</h2>
            <div className="card-arrow">↗</div>
          </article>
          <article className="outline-card takeaway-card">
            <span>03</span>
            <h2>Key<br />Takeaways</h2>
            <div className="count-mark">07</div>
          </article>
        </div>
      </section>

      <section className="takeaways section">
        <div className="section-index light">02 / Key takeaways</div>
        <div className="takeaway-list">
          {takeaways.map((item, index) => (
            <div className="takeaway-row" key={item}>
              <span>{String(index + 1).padStart(2, "0")}</span>
              <h3>{item}</h3>
              <i aria-hidden="true">↗</i>
            </div>
          ))}
        </div>
      </section>

      <section className="timeline section" id="timeline">
        <div className="section-index">03 / Action plan</div>
        <div className="timeline-heading">
          <h2>3—6—12</h2>
          <span>MONTHS</span>
        </div>
        <div className="timeline-track">
          <div className="track-line" />
          {["3", "6", "12"].map((month, index) => (
            <div className={`moment moment-${index + 1}`} key={month}>
              <div className="pulse-dot"><i /></div>
              <span>{month}</span>
              <small>MONTH{month === "3" ? "" : "S"}</small>
            </div>
          ))}
        </div>
        <div className="timeline-footer">
          <span>Approach</span>
          <span>Connect</span>
          <span>Implement</span>
        </div>
      </section>

      <section className="pathways section" id="pathways">
        <div className="section-index light">04 / Choose a pathway</div>
        <div className="pathway-grid">
          <a className="pathway emerging" href="#emerging">
            <span className="pathway-number">01</span>
            <h2>Emerging<br />Talent</h2>
            <div className="pathway-orb">
              <span>EXPLORE</span>
              <i>↗</i>
            </div>
          </a>
          <a className="pathway leaders" href="#leaders">
            <span className="pathway-number">02</span>
            <h2>Business<br />Leaders</h2>
            <div className="pathway-orb">
              <span>EXPLORE</span>
              <i>↗</i>
            </div>
          </a>
        </div>
      </section>

      <section className="branch-section emerging-branch" id="emerging">
        <div className="branch-title">
          <span>01 / Pathway</span>
          <h2>Emerging Talent</h2>
        </div>
        <div className="branch-list">
          {emerging.map((item, index) => (
            <div key={item}>
              <span>{String(index + 1).padStart(2, "0")}</span>
              <h3>{item}</h3>
              <i>+</i>
            </div>
          ))}
        </div>
      </section>

      <section className="branch-section leaders-branch" id="leaders">
        <div className="branch-title">
          <span>02 / Pathway</span>
          <h2>Business Leaders</h2>
        </div>
        <div className="branch-list">
          {leaders.map((item, index) => (
            <div key={item}>
              <span>{String(index + 1).padStart(2, "0")}</span>
              <h3>{item}</h3>
              <i>+</i>
            </div>
          ))}
        </div>
      </section>

      <footer>
        <a href="#top">CAPSTONE<span>●</span></a>
        <div className="footer-circle"><span>↑</span></div>
        <p>Outline / 2026</p>
      </footer>
    </main>
  );
}
