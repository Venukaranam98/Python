/**
 * Canvas For Hero Background
 */

export default function initCanvas() {
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  let dots = [];

  function init() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    dots = Array.from({ length: 500 }, () => ({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      r: Math.random() * 1.5,
    }));
  }

  function draw() {
    // ctx.fillStyle = "rgba(5, 5, 5, 0.2)";
    ctx.fillStyle = document.body.classList.contains("dark")
      ? "#ffffff"
      : "#000000";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    dots.forEach((d) => {
      d.x += d.vx;
      d.y += d.vy;
      if (d.x < 0 || d.x > canvas.width) d.vx *= -1;
      if (d.y < 0 || d.y > canvas.height) d.vy *= -1;
      ctx.beginPath();
      ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
      ctx.fillStyle = document.body.classList.contains("dark")
        ? "#000000"
        : "#ffffff";
      ctx.fill();
    });
    requestAnimationFrame(draw);
  }

  init();
  draw();
  window.addEventListener("resize", init);
}

export function initCanvasMain() {
  const canvasMain = document.getElementById("canvas-main");
  if (!canvasMain) return;

  const ctxMain = canvasMain.getContext("2d");
  let dots = [];

  function init() {
    const main = canvasMain.parentElement;
    canvasMain.width = main.offsetWidth;
    canvasMain.height = main.offsetHeight;

    // Create dots for main canvas
    dots = Array.from({ length: 200 }, () => ({
      x: Math.random() * canvasMain.width,
      y: Math.random() * canvasMain.height,
      vx: (Math.random() - 0.5) * 0.5,
      vy: (Math.random() - 0.5) * 0.5,
      r: Math.random() * 1.5,
    }));
  }

  function draw() {
    const isDark = document.body.classList.contains("dark");
    const dotColor = isDark ? "#f8f8fa" : "#000000";
    const bgColor = isDark ? "#000000" : "#f8f8fa";

    ctxMain.fillStyle = bgColor;
    ctxMain.fillRect(0, 0, canvasMain.width, canvasMain.height);

    dots.forEach((d) => {
      d.x += d.vx;
      d.y += d.vy;
      if (d.x < 0 || d.x > canvasMain.width) d.vx *= -1;
      if (d.y < 0 || d.y > canvasMain.height) d.vy *= -1;
      ctxMain.beginPath();
      ctxMain.arc(d.x, d.y, d.r, 0, Math.PI * 2);
      ctxMain.fillStyle = dotColor;
      ctxMain.fill();
    });

    requestAnimationFrame(draw);
  }

  init();
  draw();
  window.addEventListener("resize", init);
}
