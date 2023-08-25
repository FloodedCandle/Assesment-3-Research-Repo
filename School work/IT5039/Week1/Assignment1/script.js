document.addEventListener("DOMContentLoaded", function() {
    const display = document.getElementById("display");
    const buttons = document.querySelectorAll(".buttons button");
    const closeButton = document.getElementById("closeButton");
    const reopenButton = document.getElementById("reopenButton");
  
    let currentInput = "";
    let result = 0;
    let operator = "";
  
    closeButton.addEventListener("click", function() {
      document.body.innerHTML = "<p>Thank you for using this calculator app!</p>";
      reopenButton.style.display = "block"; // Show the "Reopen Calculator" button
    });
  
    reopenButton.addEventListener("click", function() {
      // Reset the page content to the original calculator interface
      document.body.innerHTML = `
        <div class="calculator">
          <input type="text" id="display" readonly>
          <div class="buttons">
            <!-- Buttons for digits and operations -->
          </div>
        </div>
        <button id="reopenButton" style="display: none;">Reopen Calculator</button>
        <script src="./js/script.js"></script>
      `;
  
      // Reinitialize the event listeners
      initCalculator();
    });
  
    buttons.forEach(button => {
      button.addEventListener("click", function() {
        const buttonText = this.textContent;
  
        if (buttonText >= "0" && buttonText <= "9") {
          currentInput += buttonText;
          display.value = currentInput;
        } else if (buttonText === "C") {
          clearDisplay();
        } else if (buttonText === "=") {
          evaluate();
        } else if (buttonText === "%") { // New: Modulo functionality
          if (operator === "") {
            currentInput = parseFloat(currentInput) / 100;
            display.value = currentInput;
          }
        } else {
          operator = buttonText;
          if (currentInput !== "") {
            result = parseFloat(currentInput);
            currentInput = "";
          }
        }
      });
    });
  
    function clearDisplay() {
      currentInput = "";
      result = 0;
      operator = "";
      display.value = "";
    }
  
    function evaluate() {
      if (operator === "+") {
        result += parseFloat(currentInput);
      } else if (operator === "-") {
        result -= parseFloat(currentInput);
      } else if (operator === "*") {
        result *= parseFloat(currentInput);
      } else if (operator === "/") {
        result /= parseFloat(currentInput);
      }
  
      display.value = result;
      currentInput = "";
      operator = "";
    }
  
    // Initialize the calculator app
    initCalculator();
  
    function initCalculator() {
      // ... Additional code for setting up event listeners ...
    }
  });
  