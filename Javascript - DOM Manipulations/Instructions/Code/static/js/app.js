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
button.on("click", function() {

    // clear the table
    d3.select("tbody").html("")

    //grab input element
    var inputElement = d3.select("#datetime");

    // get the value
    var inputValue = inputElement.property("value");

    // filter the data

    var filteredData  = tableData.filter(sighting => sighting.datetime === inputValue);
    
    // print in console to check
    console.log(inputValue);
    console.log(tableData);
    console.log(filteredData);

    // populate new table based on filtered data

    filteredData.forEach((obj) => {
        var row = tbody.append("tr");
        Object.entries(obj).forEach(([key, value]) => {
            var cell = row.append("td");
            cell.text(value);
        });

    })
});
