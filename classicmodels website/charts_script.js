function chart1() {
  $.ajax({
    url: "http://localhost:3001/chart1",
    type: "GET",
    success: function (data) {
      console.log(data);
      var xValues = data.xValues;
      var yValues = data.yValues;
      var barColors = ["#b91d47", "#00aba9", "#2b5797", "#e8c3b9", "#1e7145"];

      new Chart("myChart", {
        type: "doughnut",
        data: {
          labels: xValues,
          datasets: [
            {
              backgroundColor: barColors,
              data: yValues,
            },
          ],
        },
        options: {
          title: {
            display: true,
            text: "World Wide Customers",
          },
        },
      });
    },
    error: function (e) {
      $("#target").html(
        "<p class='alert alert-warning'>ERROR with REST API services. Check Developer Tools -> Console for more information.</p>"
      );
      display(e);
    },
  });
}
//SELECT year(orderDate), count(*) FROM `orders` group by year(orderDate);
//SELECT productLine, count(*) FROM `products` group by productLine ORDER BY `count(*)` DESC
//SELECT month(orderDate), count(*) FROM `orders` where year(orderDate) = 2004 group by month(orderDate) ORDER BY `month(orderDate)` ASC

function chart2() {
  const MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  $.ajax({
    url: "http://localhost:3001/chart2/2022",
    type: "GET",
    success: function (result) {
      console.log(result);

      const labels = MONTHS;
      const data = {
        labels: labels,
        datasets: [
          {
            label: "Orders",
            data: result.yValues,
            fill: false,
            borderColor: "rgb(75, 192, 192)",
            tension: 0.1,
          },
        ],
      };
      const options = {
        title: {
          display: true,
          text: "Year 2022 Orders by Month",
        },
      };
      const config = {
        type: "line",
        data: data,
        options: options,
      };
      new Chart("myChart2", config);
    },
    error: function (e) {
      $("#target").html(
        "<p class='alert alert-warning'>ERROR with REST API services. Check Developer Tools -> Console for more information.</p>"
      );
      display(e);
    },
  });
}

function chart3() {
  $.ajax({
    url: "http://localhost:3001/chart3",
    type: "GET",
    success: function (result) {
      console.log(result);

      const labels = result.xValues;
      const data = {
        labels: result.xValues,
        datasets: [
          {
            label: "Products",
            data: result.yValues,
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(255, 159, 64, 0.2)",
              "rgba(255, 205, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(201, 203, 207, 0.2)",
            ],
            borderColor: [
              "rgb(255, 99, 132)",
              "rgb(255, 159, 64)",
              "rgb(255, 205, 86)",
              "rgb(75, 192, 192)",
              "rgb(54, 162, 235)",
              "rgb(153, 102, 255)",
              "rgb(201, 203, 207)",
            ],
            borderWidth: 1,
          },
        ],
      };
      const options = {
        title: {
          display: true,
          text: "Total Products by Product Line",
        },
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      };
      const config = {
        type: "bar",
        data: data,
        options: options,
      };
      new Chart("myChart3", config);
    },
    error: function (e) {
      $("#target").html(
        "<p class='alert alert-warning'>ERROR with REST API services. Check Developer Tools -> Console for more information.</p>"
      );
      display(e);
    },
  });
}

function chart4() {
  $.ajax({
    url: "http://localhost:3001/chart4",
    type: "GET",
    success: function (result) {
      console.log(result);

      const data = {
        labels: result.xValues,
        datasets: [
          {
            label: "Orders",
            data: result.yValues,
            backgroundColor: [
              "rgb(255, 99, 132)",
              "rgb(54, 162, 235)",
              "rgb(255, 205, 86)",
            ],
            hoverOffset: 4,
          },
        ],
      };
      const options = {
        title: {
          display: true,
          text: "Total Orders in the last 3 years",
        },
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      };
      const config = {
        type: "pie",
        data: data,
        options: options,
      };
      new Chart("myChart4", config);
    },
    error: function (e) {
      $("#target").html(
        "<p class='alert alert-warning'>ERROR with REST API services. Check Developer Tools -> Console for more information.</p>"
      );
      display(e);
    },
  });
}

function chart5() {
  $.ajax({
    url: "http://localhost:3001/total_employees",
    type: "GET",
    success: function (data) {
      console.log(data.totalemployees);
      document.getElementById("totalemployees").innerHTML = data.totalemployees;
    },
    error: function (e) {
      $("#target").html(
        "<p class='alert alert-warning'>ERROR with REST API services. Check Developer Tools -> Console for more information.</p>"
      );
      display(e);
    },
  });
}
chart1();
chart2();
chart3();
chart4();
chart5();
