function load_data() {
  let searchParams = new URLSearchParams(window.location.search);
  let id = searchParams.get("id");

  $.ajax({
    url: "http://localhost:3001/employees/" + id,
    success: function (data) {
      console.log("load success, Employee name = " + data.employee_name);
      $("#employeeNumber").val(data.employeeNumber);
      $("#lastName").val(data.lastName);
      $("#firstName").val(data.firstName);
      $("#jobTitle").val(data.jobTitle);
      $("#email").val(data.email);
    },
  });
}

$(document).ready(function () {
  $("#update").on("click", function (e) {
    // Get some values from elements on the page:
    let data = {
      employeeNumber: $("#employeeNumber").val(),
      lastName: $("#lastName").val(),
      firstName: $("#firstName").val(),
      jobTitle: $("#jobTitle").val(),
      email: $("#email").val(),
    };
    console.log(JSON.stringify(data));
    $.ajax({
      url: "http://localhost:3001/employees",
      method: "PUT",
      headers: {
        Authorization: "Basic " + btoa("GBCA" + ":" + "abc!!"),
      },
      dataType: "json", //The type of data that you're expecting back from the server.
      contentType: "application/json", //When sending data to the server, use this content type.
      data: JSON.stringify(data),
      //data: data,
      success: function (data) {
        $("#target").html("<p class='alert alert-warning'>" + data + "</p>");
        console.log(data);
      },
      error: function (e) {
        $("#target").html(
          "<p class='alert alert-warning'>ERROR with REST API services. Check Developer Tools -> Console for more information.</p>"
        );
        display(e);
      },
    });
    e.preventDefault();
  });
});
