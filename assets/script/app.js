import initCanvas, { initCanvasMain } from "./canvas.js";
import DATA from "./data.js";
import { projectCardHTML, skillsIconHTML } from "./utils.js";

/* =================================================
To Toggle theme
================================================*/
function toggleTheme() {
  const toggleBtn = document.querySelector(".toggle-theme");
  const body = document.body;

  toggleBtn.addEventListener("click", () => {
    body.classList.toggle("dark");

    if (toggleBtn.firstElementChild.classList.contains("bi-sun")) {
      toggleBtn.firstElementChild.classList.replace("bi-sun", "bi-moon");
    } else {
      toggleBtn.firstElementChild.classList.replace("bi-moon", "bi-sun");
    }
  });
}

/* =================================================
To add Projects
================================================*/
function addProjects() {
  const projects = document.querySelector("#projects");

  let html = "";

  DATA.projects.forEach((project) => {
    const { title, description, image, link, tags } = project;
    html += projectCardHTML(link, image, title, description, tags);
  });

  projects.innerHTML = html;
}

/* =================================================
To add Skills
================================================*/
function addSkills() {
  const allSkills = Object.entries(DATA.skills);

  allSkills.forEach(([key, value]) => {
    let domTarget = document.querySelector(`#${key}`);
    let skills = Object.values(value);
    let skillsHTML = skills.map((skill) =>
      skillsIconHTML(skill.icon, skill.title)
    );
    domTarget.innerHTML = skillsHTML.join("");
  });
}

/* =================================================
To activate bootstrap tooltips
================================================*/
function activateBStooltip() {
  const tooltipTriggerList = document.querySelectorAll(
    '[data-bs-toggle="tooltip"]'
  );
  const tooltipList = [...tooltipTriggerList].map(
    (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
  );
}

document.addEventListener("DOMContentLoaded", function () {
  initCanvas();
  // addProjects();
  toggleTheme();
  addSkills();
  activateBStooltip();
  initCanvasMain();
});
