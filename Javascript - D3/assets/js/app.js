// Objective is to create a Scatter Plot using D3 with SVG. The plot will show how
// the relationship between the number of smokers and their age. 

// First we set the SVG width and height
var svgWidth = 960;
var svgHeight = 500;
// Then we set the margins. 
var margin = {
    top: 20,
    right: 40,
    bottom: 60,
    left: 100
};
// Calculate the width and height of the chart within SVG
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create SVG and append same to "scatter". We use #scatter because it is an ID
var svg = d3.select("#scatter")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);

// Create the chartGroup and translate it so its not on the edge
// The chartGroup is where we will be appending the data/scatter plot later
var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
d3.csv("assets/data/data.csv")
    .then(function (povertyData) {  

        // Since d3.csv returns the values as strings, we need to
        // cast them as numbers
        povertyData.forEach(function (data) {
            data.age = +data.age;
            data.smokes = +data.smokes;
        });

    // Create the scale functions. These will automatically scale the data
    // so that it fits within our chartGroup area
    var xLinearScale = d3.scaleLinear()
      .domain([30, d3.max(povertyData, d => d.age)])
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([0, d3.max(povertyData, d => d.smokes)])
      .range([height, 0]);

    // Create the axis functions to scale the x and y axes
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Append the Axes to the chart
    chartGroup.append("g")
        .attr("transform", `translate(0, ${height})`)
        .call(bottomAxis);

    chartGroup.append("g")
        .call(leftAxis);
    
    // Create the circles for each data point
    var circlesGroup = chartGroup.selectAll("circle")
        .data(povertyData)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d.age))
        .attr("cy", d => yLinearScale(d.smokes))
        .attr("r", "15")
        .attr("fill", "blue")
        .attr("opacity", ".5")

    var circleLabels = chartGroup.selectAll(null)
        .data(povertyData)
        .enter()
        .append("text");
          circleLabels
            // .attr("x", function(d) {
              // return xLinearScale(d[chosenXAxis])
            // })
            .text(d => d.abbr)
            .attr("x", d => xLinearScale(d.age))
            // .attr("x", d => xLinearScale(d[chosenXAxis]))
            .attr("y", d => yLinearScale(d.smokes))
            .attr("font-family", "sans-serif")
            .attr("font-size", "10px")
            .attr("text-anchor", "middle")
            .attr("fill", "white");
    
    // Set variable for tooltip
    var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
        return (`State: ${d.abbr}<br>Age: ${d.age}<br>Number of Smokers: ${d.smokes}`);
      });

    // call tooltip in the chartGroup
    chartGroup.call(toolTip);

    // Create event listener to display and hide tooltip
    circlesGroup.on("mouseover", function(data) {
      toolTip.show(data, this);
    })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });

    // Create and append the axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Number of Smokers");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("Smoker's Ages");
  });
