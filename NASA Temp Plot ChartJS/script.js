// data from https://data.giss.nasa.gov/gistemp_global/

get_data();
chartGraph();


async function get_data(){
    const response = await fetch("ZonAnn.Ts+dSST.csv");
    const data = await response.text();

    const xs = [];
    const y_global = [];
    const y_nhem = [];
    const y_shem = [];

    // line parse by line
    const table = data.split("\n").slice(1);

    table.forEach(elt => {

        // manual parse inz
        const columns = elt.split(",");
        const year = columns[0];

        // global temperatures
        const temp_global = columns[1]; 
        const temp_nhem = columns[2];
        const temp_shem = columns[3];

        xs.push(year);

        // pushing temperatures to arrays
        y_global.push(parseFloat(temp_global) + 14);
        y_nhem.push(parseFloat(temp_nhem) + 14);
        y_shem.push(parseFloat(temp_shem) + 14);

        console.log(year, temp_global);
    });    
    
    return {y_global, xs, y_nhem, y_shem};
}


async function chartGraph() {
    const data = await get_data();

    const ctx = document.getElementById('chart').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.xs,
            datasets: [{
                label: 'Global Average Temperature',
                data: data.y_global,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor:'rgba(255, 99, 132, 1)' ,
                borderWidth: 1,
                fill: false
            },
            {
                label: 'Northern Hemiphere Average Temperature',
                data: data.y_nhem,
                backgroundColor: 'rgba(0, 255, 132, 0.2)',
                borderColor:'rgba(0, 255, 132, 1)' ,
                borderWidth: 1,
                fill: false
            },
            {
                label: 'Southern Hemiphere Average Temperature',
                data: data.y_shem,
                backgroundColor: 'rgba(0, 0, 255, 0.2)',
                borderColor:'rgba(0, 0, 255, 1)' ,
                borderWidth: 1,
                fill: false
            }]
        },
        options: {
            scales: {
                y: {
                    ticks:{
                        callback: function(value, index, values){
                            return value + "°";
                        }
                    },
                    min: 13, 
                    max: 15.5
                    
                }
            }
        }
    });

}
