// from data.js
var tableData = data;
var button = d3.select("#filter-btn")

// get the reference to the table body
var tbody = d3.select("tbody");

// Populate the initial table with the full dataset
tableData.forEach((obj) => {
    var row = tbody.append("tr");
    Object.entries(obj).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
    });
});
// event listener for the click of button
button.on("click", function () {

    // clear the table
    d3.select("tbody").html("")

    //grab input element --- For Bonus, grab the input element for each form
    var inputDate = d3.select("#datetime").property("value");
    var inputCity = d3.select("#city").property("value");
    var inputState = d3.select("#state").property("value");
    var inputCountry = d3.select("#country").property("value");
    var inputShape = d3.select("#shape").property("value");

    // create variable to store filter

    var filter = {
        date : inputDate,
        city : inputCity,
        state : inputState,
        country : inputCountry,
        shape : inputShape
    }
    for (let val = 0; val < filter.length; val++) {
        ;
        
    }

// loop 

    filteredData = tableData.filter(function (obj) {
        Object.entries
    });


console.log(filteredData)
    // populate new table based on filtered data

    filteredData.forEach((obj) => {
        var row = tbody.append("tr");
        Object.entries(obj).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });

    })
});
