function main() {
  $.ajax({
    url: "http://localhost:3001/employees",
    type: "GET",
    headers: {
      Authorization: "Basic " + btoa("GBCA" + ":" + "abc!!"),
    },
    success: function (data) {
      // console.log(data);
      document.getElementById("content").innerHTML = "";
      $.each(data, function (key, val) {
        content = `
              <tr>
              <td scope='row'>${val.employeeNumber}</td>
              <td>${val.firstName}</td>
              <td>${val.lastName}</td>
              <td>${val.jobTitle}</td>
              <td><a href='./edit.html?id=${val.employeeNumber}'>Edit</a>, <a class='delete' href='' data-empid='${val.employeeNumber}'>Delete</a></td>
              </tr>`;
        $("#content").append(content);
        // document.getElementById("content").innerHTML += content;
      });
      $(".delete").click(function (e) {
        // alert($($(this)[0]).data("empid"));
        deleteEmployee($($(this)[0]).data("empid"));
        e.preventDefault();
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
function deleteEmployee(id) {
  $.ajax({
    url: "http://localhost:3001/employees/" + id,
    method: "DELETE",
    headers: {
      Authorization: "Basic " + btoa("GBCA" + ":" + "abc!!"),
    },
    dataType: "json",
    success: function (data) {
      $("#target").html("<p class='alert alert-warning'>" + data + "</p>");
      console.log(data);
      main();
    },
    error: function (e) {
      $("#target").html(
        "<p class='alert alert-warning'>ERROR with REST API services. Check Developer Tools -> Console for more information.</p>"
      );
      display(e);
    },
  });
}
