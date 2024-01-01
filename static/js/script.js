let themeChanger = document.getElementById("theme-changer");
let themeIcon = document.getElementById("theme-icon");

themeChanger.addEventListener("change", function (e) {
	if (this.checked) {
		themeIcon.classList.replace("fa-moon", "fa-sun");
		document.body.style.backgroundColor = "#1c1c1c";
		document.body.style.color = "#f1f1f1";
		document.querySelectorAll("small").forEach(function (topic) {
			topic.style.backgroundColor = "#f1f1f1";
			topic.style.color = "#1c1c1c";
		})
		
	} else {
		themeIcon.classList.replace("fa-sun", "fa-moon");
		document.body.style.backgroundColor = "#f1f1f1";
		document.body.style.color = "#1c1c1c";
		document.querySelectorAll("small").forEach(function (topic) {
			topic.style.backgroundColor = "#1c1c1c";
			topic.style.color = "#f1f1f1";
		})
	}
})