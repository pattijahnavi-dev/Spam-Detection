document.addEventListener("DOMContentLoaded", function () {
    const textarea = document.getElementById("message");

    if (textarea) {
        textarea.addEventListener("input", function () {
            if (this.value.length > 0) {
                this.style.borderColor = "#6366f1";
            } else {
                this.style.borderColor = "#cbd5e1";
            }
        });
    }
});
