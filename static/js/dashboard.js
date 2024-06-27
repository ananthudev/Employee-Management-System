document.addEventListener('DOMContentLoaded', function() {
  // Department Chart
  var departmentChartCtx = document.getElementById('departmentChart').getContext('2d');
  var departmentChart = new Chart(departmentChartCtx, {
      type: 'pie',
      data: {
          labels: [
              {% for stat in department_stats %}
              '{{ stat.department }}',
              {% endfor %}
          ],
          datasets: [{
              data: [
                  {% for stat in department_stats %}
                  {{ stat.count }},
                  {% endfor %}
              ],
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          responsive: true
      }
  });

  // Project Chart
  var projectChartCtx = document.getElementById('projectChart').getContext('2d');
  var projectChart = new Chart(projectChartCtx, {
      type: 'bar',
      data: {
          labels: ['Pending', 'In Progress', 'Completed'],
          datasets: [{
              data: [{{ projects_pending }}, {{ projects_inprogress }}, {{ projects_completed }}],
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(75, 192, 192, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(75, 192, 192, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });

  // Leave Chart
  var leaveChartCtx = document.getElementById('leaveChart').getContext('2d');
  var leaveChart = new Chart(leaveChartCtx, {
      type: 'doughnut',
      data: {
          labels: ['Pending', 'Approved', 'Rejected'],
          datasets: [{
              data: [{{ leaves_pending }}, {{ leaves_approved }}, {{ leaves_rejected }}],
              backgroundColor: [
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(255, 99, 132, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(255, 99, 132, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          responsive: true
      }
  });
});
