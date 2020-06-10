// from data.js
var tableData = data;

// YOUR CODE HERE!
var button = d3.select("#filter-btn");

var form = d3.select("#form");

var tbody = d3.select("tbody");


button.on("click", runEnter);
form.on("submit",runEnter);

function runEnter() {
    d3.event.preventDefault();

    var inputElement = d3.select("#datetime");
    var inputElement2 = d3.select("#cityname");
    var inputElement3 = d3.select("#shapename");

    var inputValue = inputElement.property("value");
    var inputValue2 = inputElement2.property("value");
    var inputValue3 = inputElement3.property("value");
    
    console.log(inputValue);
    console.log(inputValue2);
    console.log(inputValue3);
    console.log(tableData);

    // var filteredData = tableData.filter(ufo => (ufo.shape === inputValue3));

    var filteredData = tableData.filter(ufo => (ufo.datetime === inputValue)&&(ufo.city === inputValue2)&&(ufo.shape === inputValue3));

    console.log(filteredData);

    filteredData.forEach((ufodata) => {
        var row = tbody.append("tr");
        Object.entries(ufodata).forEach(([key, value]) => {
          var cell = row.append("td");
          cell.text(value);
        });
      });

  
};



