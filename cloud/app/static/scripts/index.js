function Drawer() {
  document.getElementById("drawer").classList.remove("hidden");
  document.getElementById("drawer").classList.add("visible");
}

function hide_drawer() {
  document.getElementById("drawer").classList.remove("visible");
  document.getElementById("drawer").classList.add("hidden");
}

document.addEventListener("click", function (e) {
  const drawer = document.getElementById("drawer");
  if (e.target === drawer) {
    hide_drawer();
  }
});
function show_gallerry() {
  document.getElementById("gallery").classList.remove("hidden");
  document.getElementById("gallery").classList.add("visible");
}

var accordion = document.getElementsByClassName("accordion");
for (var i = 0; i < accordion.length; i++) {
  accordion[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    if (panel.style.display === "block") {
      panel.style.display = "none";
    } else {
      panel.style.display = "block";
    }
  });
}

function RegDownload(type, val) {
  // Data received from clients for development/design improvemets
  window.location.href =
    val + `?ext=${type}&plt=${navigator.platform}&usgt=${navigator.userAgent}`;
}
