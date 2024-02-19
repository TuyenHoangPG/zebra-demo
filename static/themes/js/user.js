const hostUrl =
  "http://" + document.location.hostname + ":" + window.location.port;
const apiUrl = "/api/bookings/";

const uri = `https://api.github.com/search/users?q=type%3Auser`;
const table = new DataTable("#user-table", {
  ajax: { url: uri, dataSrc: "items" },
  dataType: "json",
  contentType: "application/json; charset=utf-8",
  type: "GET",
  processing: true,
  columns: [{ data: "login" }, { data: "id" }],
});

document.querySelectorAll("a.toggle-vis").forEach((el) => {
  el.addEventListener("click", function (e) {
    e.preventDefault();

    let columnIdx = e.target.getAttribute("data-column");
    let column = table.column(columnIdx);

    // Toggle the visibility
    column.visible(!column.visible());
  });
});
