document.addEventListener("DOMContentLoaded", function () {

    const resumeInput = document.querySelector('input[name="resume"]');
    const form = document.querySelector("form");

    // Display selected PDF filename
    if (resumeInput) {
        resumeInput.addEventListener("change", function () {

            const file = this.files[0];

            if (file) {
                if (!file.name.toLowerCase().endsWith(".pdf")) {
                    alert("Please upload a PDF file.");
                    this.value = "";
                    return;
                }

                alert("Selected file: " + file.name);
            }
        });
    }

    // Validate form before submission
    if (form) {
        form.addEventListener("submit", function (event) {

            const jobDescription =
                document.querySelector('textarea[name="job_description"]');

            if (!resumeInput.files.length) {
                alert("Please upload your resume.");
                event.preventDefault();
                return;
            }

            if (!jobDescription.value.trim()) {
                alert("Please enter a job description.");
                event.preventDefault();
            }
        });
    }

});