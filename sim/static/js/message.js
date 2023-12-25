$(document).ready(function(){
    var alertTimeout = 5000; 
    var alertID = '#myAlert';
    var progressBarID = '#progressBarInner';

    function hideAlert() {
        $(alertID).alert('close');
    }

    setTimeout(hideAlert, alertTimeout);

    function updateProgressBar() {
        var currentTime = new Date().getTime();
        var elapsedTime = currentTime - startTime;
        var progress = ((alertTimeout - elapsedTime) / alertTimeout) * 100;
        
        if (progress < 0) {
            progress = 0;
        }

        $(progressBarID).css('width', progress + '%').attr('aria-valuenow', progress);
    }

    var startTime = new Date().getTime();

    var progressBarInterval = setInterval(updateProgressBar, 100);
});