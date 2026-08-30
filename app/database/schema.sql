CREATE TABLE IF NOT EXISTS users (
    id CHAR(36) PRIMARY KEY,
    fullname VARCHAR(120) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(30) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL,
    CHECK (role IN ('patient', 'doctor', 'admin'))
);

CREATE TABLE IF NOT EXISTS patients (
    id CHAR(36) PRIMARY KEY,
    date_of_birth DATE NOT NULL,
    gender VARCHAR(30) NOT NULL,
    address VARCHAR(255) NOT NULL,
    reason VARCHAR(255),
    CONSTRAINT fk_patient_user FOREIGN KEY (id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS doctors (
    id CHAR(36) PRIMARY KEY,
    specialization VARCHAR(120) NOT NULL,
    CONSTRAINT fk_doctor_user FOREIGN KEY (id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS appointments (
    appointment_id CHAR(36) PRIMARY KEY,
    patient_id CHAR(36) NOT NULL,
    doctor_id CHAR(36) NOT NULL,
    appointment_datetime DATETIME NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'scheduled',
    reason VARCHAR(255),
    created_at DATETIME NOT NULL,
    CONSTRAINT fk_appointment_patient FOREIGN KEY (patient_id) REFERENCES patients(id) ON DELETE CASCADE,
    CONSTRAINT fk_appointment_doctor FOREIGN KEY (doctor_id) REFERENCES doctors(id) ON DELETE CASCADE,
    CHECK (status IN ('scheduled', 'confirmed', 'completed', 'cancelled', 'no_show'))
);

CREATE INDEX idx_appointments_patient ON appointments(patient_id);
CREATE INDEX idx_appointments_doctor_time ON appointments(doctor_id, appointment_datetime);