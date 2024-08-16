document.addEventListener("DOMContentLoaded", function() {
    var feedbackButton = document.getElementById("feedbackButton");
    var feedbackPopup = document.getElementById("feedbackPopup");
    var closeBtn = document.querySelector(".close");
    var submitFeedback = document.getElementById("submitFeedback");

    feedbackButton.onclick = function() {
        feedbackPopup.style.display = "flex";
    };

    closeBtn.onclick = function() {
        feedbackPopup.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == feedbackPopup) {
            feedbackPopup.style.display = "none";
        }
    };

    submitFeedback.onclick = function() {
        var feedbackText = document.getElementById("feedbackText").value;
        if (feedbackText) {
            text1 = 'mailto:ithamar.kaplan@gmail.com?subject=Feedback&body=';
            window.open(text1.concat(feedbackText));
            feedbackPopup.style.display = "none";
            document.getElementById("feedbackText").value = ""; // Clear the textarea
        } else {
            alert("Please enter your feedback before submitting.");
        }
    };
});