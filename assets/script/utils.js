/* =================================== 
PROJECT CARD HTML STRUCTURE
=================================== */
export function projectCardHTML(link, image, title, description, tags) {
  return `<div class="col-xl-6">
      <div
        class="card project-card border-0 p-1 m-2"
        style="box-shadow: var(--shadow-sm)"
      >
        <div class="link-wrapper">
          <a href="${link}">
            <i class="bi bi-arrow-right"></i>
          </a>
        </div>
        <div class="row g-0">
          <div class="col-md-5">
            <div class="card-img-wrapper">
              <img src="${image}" alt="${title}" />
            </div>
          </div>
          <div class="col-md-7 card-body text-start align-self-center">
            <h4 class="card-title text-capitalize">${title}</h4>
            <p
              class="card-text truncate-4-lines small"
              style="color: var(--text-secondary)"
            >
              ${description}
            </p>
            <div class="card-badges">
              ${tags
                .map((tag) => `<div class="badge text-lowercase my-1">${tag}</div>`)
                .join(" ")}
            </div>
          </div>
        </div>
      </div>
    </div>`;
}

/* =================================== 
SKILL ICONS HTML STRUCTURE
=================================== */
export function skillsIconHTML(iconSrc, name) {
  return `<div class="icon">
      <img
        src="${iconSrc}"
        alt="${name}"
        data-bs-custom-class="custom-tooltip"
        data-bs-toggle="tooltip"
        data-bs-placement="top"
        data-bs-title="${name}"
        lazy="eager"
      />
    </div>`;
}
