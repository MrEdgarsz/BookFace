window.addEventListener("scroll", () => {
    const scrolled = window.scrollY;
    const btnScrollToTop = document.querySelector("#btnScrollToTop");

    if (scrolled < 500) {
        return btnScrollToTop.style.display = "none";
    }

    btnScrollToTop.style.display = "block";
    btnScrollToTop.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            left: 0,
            behavior: "smooth"
        });
    });
});