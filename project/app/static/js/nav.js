document.addEventListener("DOMContentLoaded", () => {
  if (
    window.location.pathname.includes("trade") ||
    window.location.pathname.includes("write") ||
    window.location.pathname.includes("edit")
  ) {
    document.getElementById("trade-button").classList.toggle("orange-text");
  } else if (window.location.pathname == "/location/") {
    document.getElementById("location-button").classList.toggle("orange-text");
  } else if (window.location.pathname == "/jobs/") {
    document.getElementById("jobs-button").classList.toggle("orange-text");
  } else if (window.location.pathname == "/realty/") {
    document.getElementById("realty-button").classList.toggle("orange-text");
  }
});
