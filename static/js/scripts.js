document.addEventListener("DOMContentLoaded", function () {
    function setupCarousel(carouselInnerId) {
        const carouselInner = document.getElementById(carouselInnerId);
        const items = Array.from(carouselInner.querySelectorAll(".carousel-item"));

        if (!carouselInner || items.length === 0) return;

        carouselInner.innerHTML = "";

        const groupSize = 3;

        for (let i = 0; i < items.length; i += groupSize) {
            const newItem = document.createElement("div");
            newItem.classList.add("carousel-item");
            if (i === 0) newItem.classList.add("active");

            const rowDiv = document.createElement("div");
            rowDiv.classList.add("row", "justify-content-center", "gx-3", "py-4");

            for (let j = i; j < i + groupSize && j < items.length; j++) {
                const card = items[j].querySelector(".card");
                if (card) {
                    const clonedCard = card.cloneNode(true);

                    const colDiv = document.createElement("div");
                    colDiv.classList.add("col-12", "col-md-6", "col-lg-4", "d-flex");

                    clonedCard.classList.add("h-100");
                    clonedCard.style.width = "100%";

                    colDiv.appendChild(clonedCard);
                    rowDiv.appendChild(colDiv);
                }
            }

            newItem.appendChild(rowDiv);
            carouselInner.appendChild(newItem);
        }
    }

    // Setup both carousels
    setupCarousel("carousel-inner"); // for audioGearCarousel
    setupCarousel("charger-carousel-inner"); // for chargerCarousel
});
