$(document).ready(function () {
  console.log("document ready");

  $("#save").on("click", function (e) {
    // Get some values from elements on the page:
    let data = {
      lastName: $("#lastName").val(),
      firstName: $("#firstName").val(),
      jobTitle: $("#jobTitle").val(),
      email: $("#email").val(),
    };
    console.log(JSON.stringify(data));
    $.ajax({
      url: "http://localhost:3001/employees",
      method: "POST",
      headers: {
        Authorization: "Basic " + btoa("GBCA" + ":" + "abc!!"),
      },
      dataType: "json", //The type of data that you're expecting back from the server.
      contentType: "application/json", //When sending data to the server, use this content type.
      data: JSON.stringify(data),
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
