const phrases = ["secure REST APIs.", "Django applications.", "PostgreSQL-backed systems.", "clean admin dashboards."];
const typedText = document.getElementById("typedText");
let phraseIndex = 0;
let charIndex = 0;
let deleting = false;

function typeLoop() {
    if (!typedText) return;
    const current = phrases[phraseIndex];
    typedText.textContent = current.slice(0, charIndex);

    if (!deleting && charIndex < current.length) {
        charIndex += 1;
        setTimeout(typeLoop, 85);
        return;
    }

    if (!deleting && charIndex === current.length) {
        deleting = true;
        setTimeout(typeLoop, 1400);
        return;
    }

    if (deleting && charIndex > 0) {
        charIndex -= 1;
        setTimeout(typeLoop, 35);
        return;
    }

    deleting = false;
    phraseIndex = (phraseIndex + 1) % phrases.length;
    setTimeout(typeLoop, 250);
}

function applyTheme(theme) {
    document.documentElement.dataset.theme = theme;
    localStorage.setItem("portfolio-theme", theme);
    const icon = document.querySelector("#themeToggle i");
    if (icon) {
        icon.className = theme === "dark" ? "bi bi-sun" : "bi bi-moon-stars";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    typeLoop();
    const savedTheme = localStorage.getItem("portfolio-theme") || "dark";
    applyTheme(savedTheme);

    document.getElementById("themeToggle")?.addEventListener("click", () => {
        const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        applyTheme(nextTheme);
    });
});
