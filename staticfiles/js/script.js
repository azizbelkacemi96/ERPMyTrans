$(document).ready(function() {
  // Configuration de Select2 pour l'affichage de la liste des employés
  $(".select2").select2({
    placeholder: "Sélectionnez un ou plusieurs employés",
    allowClear: true
  });

  // Configuration de la fonction de recherche
  $("#search").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#employee-list .employee-card").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  // Ajout de l'employé sélectionné à la liste des employés de la mission
  $("#add-employee-btn").on("click", function() {
    var employeeId = $(".select2").val();
    var employeeName = $(".select2 option:selected").text();

    if (employeeId && employeeName) {
      var listItem = $("<li></li>").addClass("list-group-item d-flex justify-content-between align-items-center").text(employeeName);
      var hiddenInput = $("<input>").attr({
        type: "hidden",
        name: "employees",
        value: employeeId
      });
      var deleteBtn = $("<button></button>").addClass("btn btn-danger btn-sm delete-employee-btn").html("&times;");
      listItem.append(hiddenInput);
      listItem.append(deleteBtn);
      $("#employee-list-selected").append(listItem);
      $(".select2 option[value='" + employeeId + "']").remove();
      $(".select2").val(null).trigger("change");
    }
  });

  // Suppression de l'employé de la liste des employés de la mission
  $("#employee-list-selected").on("click", ".delete-employee-btn", function() {
    var employeeId = $(this).siblings("input").val();
    var employeeName = $(this).siblings("span").text();
    var option = $("<option></option>").val(employeeId).text(employeeName);
    $("#employees").append(option);
    $(this).parent().remove();
  });
});
