// Variável para armazenar o valor lido
int sensorPin = A0;  // Pino analógico conectado ao sensor
int sensorValue = 0; 
void setup() {
  Serial.begin(9600); 
  int sensorPin = A0;  // Pino analógico conectado ao sensor
  int sensorValue = 0; // Inicia comunicação serial
}

void loop() {
  sensorValue = analogRead(sensorPin); // Lê o valor do sensor
  Serial.print("Leitura: ");
  Serial.println(sensorValue); // Exibe no monitor serial
  delay(1000); // Espera 1 segundo
}
