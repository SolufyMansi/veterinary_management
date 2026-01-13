
// frappe.pages['appointment-history'].on_page_load = function (wrapper) {

//     const page = frappe.ui.make_app_page({
//         parent: wrapper,
//         title: 'Appointment History',
//         single_column: true
//     });

//     // Inject styles
//     $('<style>').html(`
//         .filter-bar {
//             display: flex;
//             gap: 15px;
//             padding: 15px;
//             align-items: center;
//         }

//         .appointment-container {
//             display: grid;
//             grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
//             gap: 20px;
//             padding: 15px;
//         }

//         .appointment-card {
//             padding: 18px;
//             border-radius: 14px;
//             color: #fff;
//             box-shadow: 0 10px 18px rgba(0,0,0,0.15);
//         }

//         .status-open {
//             background: linear-gradient(135deg, #1e3c72, #2a5298);
//         }

//         .status-completed {
//             background: linear-gradient(135deg, #1d976c, #93f9b9);
//             color: #083b2f;
//         }

//         .status-cancelled {
//             background: linear-gradient(135deg, #434343, #b71c1c);
//         }

//         .appointment-card h4 {
//             font-size: 17px;
//             margin-bottom: 8px;
//         }

//         .appointment-card p {
//             margin: 4px 0;
//             font-size: 14px;
//         }

//         .card-btn {
//             margin-top: 12px;
//         }
//     `).appendTo("head");

//     // Filters + container
//     $(page.main).append(`
//         <div class="filter-bar">
//             <input type="date" id="filter-date" class="form-control" style="max-width:200px">
//             <select id="filter-status" class="form-control" style="max-width:200px">
//                 <option value="">All Status</option>
//                 <option value="Open">Open</option>
//                 <option value="Completed">Completed</option>
//                 <option value="Cancelled">Cancelled</option>
//             </select>
//         </div>

//         <div class="appointment-container" id="appointment-container"></div>
//     `);

//     // Filter events
//     $("#filter-date, #filter-status").on("change", function () {
//         load_appointments();
//     });

//     load_appointments();
// };

// function load_appointments() {
//     frappe.call({
//         method: "veterinary_management.veterinary_management.page.appointment_history.appointment_history.get_appointments",
//         args: {
//             date: $("#filter-date").val(),
//             status: $("#filter-status").val()
//         },
//         callback: function (r) {
//             const container = $("#appointment-container");
//             container.empty();

//             if (!r.message || r.message.length === 0) {
//                 container.append(`<p class="text-muted">No Appointments Found</p>`);
//                 return;
//             }

//             r.message.forEach(app => {
//                 let status_class = "status-open";
//                 if (app.status === "Completed") status_class = "status-completed";
//                 if (app.status === "Cancelled") status_class = "status-cancelled";

//                 container.append(`
//                     <div class="appointment-card ${status_class}">
//                         <h4>${app.name}</h4>

//                         <p><strong>Pet:</strong> ${app.customer_name || "-"}</p>
//                         <p><strong>Date:</strong> ${app.custom_scheduled_date}</p>
//                         <p><strong>Time:</strong> ${app.custom_schedule_time || "-"}</p>
//                         <p><strong>Doctor:</strong> ${app.custom_doctor || "-"}</p>

//                         <p><strong>Status:</strong> ${app.status}</p>

//                         <div class="card-btn">
//                             <button class="btn btn-sm btn-light"
//                                 onclick="frappe.set_route('Form','Appointment','${app.name}')">
//                                 View
//                             </button>
//                         </div>
//                     </div>
//                 `);
//             });
//         }
//     });
// }
frappe.pages['appointment-history'].on_page_load = function (wrapper) {

    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Appointment History',
        single_column: true
    });

    $('<style>').html(`
        .filter-bar {
            display: flex;
            gap: 14px;
            padding: 14px;
            align-items: center;
        }

        .appointment-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 14px;
            padding: 14px;
        }

        .appointment-card {
            background: #ffffff;
            border-radius: 10px;
            padding: 14px 16px;
            border-left: 5px solid #dee2e6;
            box-shadow: 0 4px 8px rgba(0,0,0,0.06);
        }

        .status-scheduled { border-left-color: #5c7cfa; }
        .status-in-process { border-left-color: #f59f00; }
        .status-completed { border-left-color: #20c997; }
        .status-cancelled { border-left-color: #fa5252; }

        .appointment-card h4 {
            font-size: 15px;
            font-weight: 600;
            margin-bottom: 6px;
            color: #212529;
        }

        .appointment-card p {
            margin: 3px 0;
            font-size: 13px;
            color: #495057;
        }

        .status-text {
            font-weight: 600;
        }

        .status-scheduled .status-text { color: #5c7cfa; }
        .status-in-process .status-text { color: #f59f00; }
        .status-completed .status-text { color: #20c997; }
        .status-cancelled .status-text { color: #fa5252; }

        .card-btn {
            margin-top: 10px;
        }
    `).appendTo("head");

    $(page.main).append(`
        <div class="filter-bar">
            <input type="date" id="filter-date" class="form-control" style="max-width:200px">

            <select id="filter-status" class="form-control" style="max-width:200px">
                <option value="">All Status</option>
                <option value="Scheduled">Scheduled</option>
                <option value="In Process">In Process</option>
                <option value="Completed">Completed</option>
                <option value="Cancelled">Cancelled</option>
            </select>
        </div>

        <div class="appointment-container" id="appointment-container"></div>
    `);

    $("#filter-date, #filter-status").on("change", load_appointments);

    load_appointments();
};

function load_appointments() {
    frappe.call({
        method: "veterinary_management.veterinary_management.page.appointment_history.appointment_history.get_appointments",
        args: {
            date: $("#filter-date").val(),
            status: $("#filter-status").val()
        },
        callback: function (r) {
            const container = $("#appointment-container");
            container.empty();

            if (!r.message || r.message.length === 0) {
                container.append(`<p class="text-muted">No Appointments Found</p>`);
                return;
            }

            r.message.forEach(app => {

                let status_class = "status-scheduled";
                if (app.status === "In Process") status_class = "status-in-process";
                else if (app.status === "Completed") status_class = "status-completed";
                else if (app.status === "Cancelled") status_class = "status-cancelled";

                container.append(`
                    <div class="appointment-card ${status_class}">
                        <h4>${app.name}</h4>

                        <p><strong>Pet:</strong> ${app.customer_name || "-"}</p>
                        <p><strong>Date:</strong> ${app.custom_scheduled_date}</p>
                        <p><strong>Time:</strong> ${app.custom_schedule_time || "-"}</p>
                        <p><strong>Doctor:</strong> ${app.custom_doctor_name || "-"}</p>

                        <p>
                            <strong>Status:</strong>
                            <span class="status-text">${app.status}</span>
                        </p>

                        <div class="card-btn">
                            <button class="btn btn-sm btn-outline-primary"
                                onclick="frappe.set_route('Form','Appointment','${app.name}')">
                                View
                            </button>
                        </div>
                    </div>
                `);
            });
        }
    });
}
