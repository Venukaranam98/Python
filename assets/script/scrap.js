document.addEventListener("DOMContentLoaded", function () {
  drawCanvas();
  toggleTheme();
  initProjects();
});

/*================================================
Canvas
================================================*/



function initProjects() {
  const card = `<div class="col-xl-6">
      <div
        class="card project-card border-0 p-1 m-2"
        style="box-shadow: var(--shadow-sm)"
      >
        <div class="link-wrapper">
          <a href="#">
            <i class="bi bi-arrow-right"></i>
          </a>
        </div>
        <div class="row g-0">
          <div class="col-md-5">
            <div class="card-img-wrapper">
              <img src="./image.png" alt="" />
            </div>
          </div>
          <div class="col-md-7 card-body text-start">
            <h4 class="card-title">Single Vendor Ecommerce Site</h4>
            <p
              class="card-text truncate-4-lines"
              style="color: var(--text-secondary)"
            >
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde
              aliquam illum animi blanditiis saepe rerum quibusdam repellendus
              similique, ab debitis quis nisi, perferendis molestiae sed nihil
              suscipit incidunt temporibus nobis.
            </p>
            <div class="card-badges">
              <div class="badge">React JS</div>
              <div class="badge">Firebase</div>
              <div class="badge">web workers</div>
              <div class="badge">razorpay</div>
              <div class="badge">shipping rocket</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;

  const projects = document.querySelector("#projects");
  for (let i = 0; i < 3; i++) {
    projects.innerHTML += card;
  }
}
