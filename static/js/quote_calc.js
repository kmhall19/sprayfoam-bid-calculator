document.addEventListener('DOMContentLoaded', function () {
    const types = ['open', 'closed', 'hybrid'];
  
    // Set default values (you can override these by rendering them via Django)
    const costSettings = {
      open: {
        materialCostPerBoardFoot: parseFloat(document.getElementById('open_material_cost').dataset.default) || 0.30,
        laborRatePerHour: parseFloat(document.getElementById('open_labor_rate').dataset.default) || 50,
        coveragePerSet: parseFloat(document.getElementById('open_coverage').dataset.default) || 16000
      },
      closed: {
        materialCostPerBoardFoot: parseFloat(document.getElementById('closed_material_cost').dataset.default) || 0.70,
        laborRatePerHour: parseFloat(document.getElementById('closed_labor_rate').dataset.default) || 60,
        coveragePerSet: parseFloat(document.getElementById('closed_coverage').dataset.default) || 4000
      },
      hybrid: {
        materialCostPerBoardFoot: parseFloat(document.getElementById('hybrid_material_cost').dataset.default) || 0.50,
        laborRatePerHour: parseFloat(document.getElementById('hybrid_labor_rate').dataset.default) || 55,
        coveragePerSet: parseFloat(document.getElementById('hybrid_coverage').dataset.default) || 8000
      }
    };
  
    // Hook into all input fields to recalculate on change
    types.forEach(type => {
      const inputFields = document.querySelectorAll(`input[data-type="${type}"]`);
      inputFields.forEach(field => {
        field.addEventListener('input', () => {
          calculateQuote(type);
        });
      });
    });
  
    function calculateQuote(type) {
      const sets = parseFloat(document.getElementById(`${type}_sets`).value) || 0;
      const laborHours = parseFloat(document.getElementById(`${type}_labor_hours`).value) || 0;
  
      const boardFeet = sets * costSettings[type].coveragePerSet;
      const materialCost = boardFeet * costSettings[type].materialCostPerBoardFoot;
      const laborCost = laborHours * costSettings[type].laborRatePerHour;
      const totalCost = materialCost + laborCost;
  
      // Update display fields
      document.getElementById(`${type}_board_feet`).value = boardFeet.toFixed(2);
      document.getElementById(`${type}_material_cost`).value = materialCost.toFixed(2);
      document.getElementById(`${type}_labor_cost`).value = laborCost.toFixed(2);
      document.getElementById(`${type}_total_cost`).value = totalCost.toFixed(2);
    }
  
    // Trigger initial calculation for all types
    types.forEach(type => calculateQuote(type));
  });
  