// ================================
// HDI Prediction Form Validation
// ================================

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (!form) return;

    form.addEventListener("submit", function (event) {

        const lifeExpectancy = parseFloat(document.getElementsByName("life_expectancy")[0].value);
        const expectedSchooling = parseFloat(document.getElementsByName("expected_schooling")[0].value);
        const meanSchooling = parseFloat(document.getElementsByName("mean_schooling")[0].value);
        const gni = parseFloat(document.getElementsByName("gni")[0].value);

        // Check for empty values
        if (
            isNaN(lifeExpectancy) ||
            isNaN(expectedSchooling) ||
            isNaN(meanSchooling) ||
            isNaN(gni)
        ) {
            alert("Please fill in all the fields.");
            event.preventDefault();
            return;
        }

        // Validate ranges
        if (lifeExpectancy < 40 || lifeExpectancy > 90) {
            alert("Life Expectancy should be between 40 and 90.");
            event.preventDefault();
            return;
        }

        if (expectedSchooling < 0 || expectedSchooling > 25) {
            alert("Expected Years of Schooling should be between 0 and 25.");
            event.preventDefault();
            return;
        }

        if (meanSchooling < 0 || meanSchooling > 20) {
            alert("Mean Years of Schooling should be between 0 and 20.");
            event.preventDefault();
            return;
        }

        if (gni < 0) {
            alert("Gross National Income cannot be negative.");
            event.preventDefault();
            return;
        }

    });

});