

fetch('/analysis')
.then(response => response.json())
.then(data => {

    document.getElementById('max').innerHTML =
        data.max_temp + "°C";

    document.getElementById('min').innerHTML =
        data.min_temp + "°C";

    document.getElementById('avg').innerHTML =
        data.avg_temp + "°C";

    document.getElementById('days').innerHTML =
        data.total_days;
});


// Load Chart

fetch('/chart')
.then(response => response.json())
.then(data => {

    const ctx =
    document.getElementById('tempChart');

    new Chart(ctx, {

        type:'line',

        data:{
            labels:data.dates,

            datasets:[{

                label:'Temperature',

                data:data.temps,

                borderWidth:3,
                fill:false
            }]
        }
    });
});


// Prediction

function predictTemperature(){

    let day =
    document.getElementById('futureDay').value;

    let formData =
    new FormData();

    formData.append("day", day);

    fetch('/predict',{

        method:'POST',
        body:formData
    })

    .then(response => response.json())

    .then(data => {

        document.getElementById(
        'predictionResult'
        ).innerHTML =

        "Predicted Temperature: " +
        data.predicted_temperature +
        " °C";
    });
}
