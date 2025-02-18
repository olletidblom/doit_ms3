document.addEventListener("DOMContentLoaded", function () {
    let messageContainer = document.querySelector(".messages");

    if (messageContainer) {
        messageContainer.addEventListener("click", function (event) {
            if (event.target.classList.contains("btn-close")) {
                let alertBox = event.target.closest(".alert");
                alertBox.remove(); // Remove the specific alert

                // If no alerts are left, remove the entire .messages container
                if (document.querySelectorAll(".messages .alert").length === 0) {
                    messageContainer.remove();
                }
            }
        });
    }
});