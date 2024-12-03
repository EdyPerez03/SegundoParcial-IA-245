
--  Oracle
-- Crear tabla de Autos
CREATE TABLE Autos (
    id_auto NUMBER PRIMARY KEY,
    modelo VARCHAR2(100),
    descripcion CLOB,
    precio NUMBER(15, 2),
    stock NUMBER
);

-- Crear tabla de Clientes
CREATE TABLE Clientes (
    id_cliente NUMBER PRIMARY KEY,
    nombre VARCHAR2(100),
    correo VARCHAR2(100),
    direccion VARCHAR2(200),
    telefono VARCHAR2(20)
);

-- Crear tabla de Ventas
CREATE TABLE Ventas (
    id_venta NUMBER PRIMARY KEY,
    id_cliente NUMBER,
    fecha_venta DATE,
    total NUMBER(15, 2),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente)
);

-- Crear tabla de Detalles de la Venta
CREATE TABLE Detalles_Venta (
    id_detalle NUMBER PRIMARY KEY,
    id_venta NUMBER,
    id_auto NUMBER,
    cantidad NUMBER,
    precio_unitario NUMBER(15, 2),
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta),
    FOREIGN KEY (id_auto) REFERENCES Autos(id_auto)
);

BEGIN
    
     -- Insertar datos en la tabla de Autos
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (1, 'Ferrari Roma', 'Coupé de lujo con motor V8 de 620 hp', 220000.00, 5);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (2, 'Ferrari 488 GTB', 'Deportivo con motor V8 biturbo de 670 hp', 280000.00, 3);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (3, 'Ferrari SF90 Stradale', 'Híbrido con motor V8 y 3 motores eléctricos, 1000 hp', 500000.00, 2);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (4, 'Ferrari 458 Italia', 'Deportivo con motor V8 atmosférico de 570 hp', 250000.00, 4);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (5, 'Ferrari 812 Superfast', 'Coupé de lujo con motor V12 de 800 hp', 350000.00, 4);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (6, 'Ferrari F8 Tributo', 'Deportivo con motor V8 biturbo de 710 hp', 300000.00, 6);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (7, 'Ferrari Portofino M', 'Cabrio con motor V8 biturbo de 620 hp', 230000.00, 5);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (8, 'Ferrari LaFerrari', 'Híbrido con motor V12 y eléctrico de 950 hp', 1500000.00, 2);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (9, 'Ferrari GTC4Lusso', 'Coupé de lujo con motor V12 de 680 hp', 350000.00, 3);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (10, 'Ferrari California T', 'Convertible con motor V8 biturbo de 560 hp', 220000.00, 4);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (11, 'Ferrari 488 Pista', 'Deportivo con motor V8 biturbo de 710 hp', 350000.00, 3);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (12, 'Ferrari F12 Berlinetta', 'Coupé con motor V12 de 740 hp', 320000.00, 4);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (13, 'Ferrari Monza SP2', 'Edición limitada con motor V12 de 810 hp', 1200000.00, 2);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (14, 'Ferrari 246 Dino', 'Clásico deportivo con motor V6 de 180 hp', 250000.00, 5);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (15, 'Ferrari Enzo', 'Deportivo exclusivo con motor V12 de 651 hp', 1200000.00, 1);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (16, 'Ferrari Testarossa', 'Clásico deportivo con motor V12 de 390 hp', 200000.00, 2);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (17, 'Ferrari FF', 'Coupé con motor V12 de 651 hp y tracción total', 300000.00, 3);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (18, 'Ferrari SP38', 'Deportivo único basado en el 488 GTB, motor V8', 2500000.00, 1);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (19, 'Ferrari F40', 'Ícono de los 80 con motor V8 biturbo de 478 hp', 1500000.00, 2);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (20, 'Ferrari F50', 'Edición especial con motor V12 de 513 hp', 2000000.00, 1);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (21, 'Ferrari Daytona SP3', 'Coupé exclusivo con motor V12 de 828 hp', 2200000.00, 2);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (22, 'Ferrari 296 GTB', 'Híbrido con motor V6 biturbo y eléctrico, 830 hp', 320000.00, 5);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (23, 'Ferrari 275 GTB', 'Clásico de los 60 con motor V12 de 280 hp', 2000000.00, 1);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (24, 'Ferrari Purosangue', 'SUV de lujo con motor V12 de 715 hp', 400000.00, 6);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (25, 'Ferrari 812 Competizione', 'Edición limitada con motor V12 de 830 hp', 700000.00, 3);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (26, 'Ferrari J50', 'Edición especial con motor V8 biturbo de 690 hp', 3000000.00, 1);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (27, 'Ferrari 308 GTS', 'Clásico de los 80 con motor V8 de 255 hp', 150000.00, 4);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (28, 'Ferrari SP1 Monza', 'Edición limitada con motor V12 de 810 hp', 1500000.00, 2);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (29, 'Mazda MX-5 Miata', 'Roadster compacto con motor de 181 hp', 28000.00, 10);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (30, 'Ford Mustang EcoBoost', 'Coupé deportivo con motor turbo de 310 hp', 27000.00, 8);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (31, 'Chevrolet Camaro LT', 'Deportivo con motor V6 de 335 hp', 29000.00, 6);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (32, 'Toyota GR Supra', 'Coupé deportivo con motor turbo de 382 hp', 44000.00, 5);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (33, 'Subaru BRZ', 'Deportivo ligero con motor de 228 hp', 30000.00, 7);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (34, 'Honda Civic Type R', 'Hatchback deportivo con motor turbo de 315 hp', 44000.00, 6);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (35, 'Volkswagen Golf R', 'Hatchback deportivo con tracción integral y 315 hp', 45000.00, 6);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (36, 'Nissan 370Z', 'Coupé deportivo con motor V6 de 332 hp', 35000.00, 4);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (37, 'Hyundai Veloster N', 'Hatchback deportivo con motor turbo de 276 hp', 35000.00, 5);
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (38, 'Kia Stinger GT', 'Sedán deportivo con motor V6 biturbo de 368 hp', 53000.00, 4);


    -- Insertar datos en la tabla de Clientes
    INSERT INTO Clientes (id_cliente, nombre, correo, direccion, telefono) VALUES
    (1, 'Carlos Martínez', 'carlos.martinez@gmail.com', 'Av. Ferrari 123, Ciudad', '1122334455');
    
    INSERT INTO Clientes (id_cliente, nombre, correo, direccion, telefono) VALUES
    (2, 'Lucía Gómez', 'lucia.gomez@yahoo.com', 'Calle Larga 456, Ciudad', '6677889900');

    -- Insertar datos en la tabla de Ventas
    INSERT INTO Ventas (id_venta, id_cliente, fecha_venta, total) VALUES
    (1, 1, TO_DATE('2024-12-01', 'YYYY-MM-DD'), 500000.00);
    
    INSERT INTO Ventas (id_venta, id_cliente, fecha_venta, total) VALUES
    (2, 2, TO_DATE('2024-12-02', 'YYYY-MM-DD'), 280000.00);

    -- Insertar datos en la tabla de Detalles de la Venta
    INSERT INTO Detalles_Venta (id_detalle, id_venta, id_auto, cantidad, precio_unitario) VALUES
    (1, 1, 3, 1, 500000.00);
    
    INSERT INTO Detalles_Venta (id_detalle, id_venta, id_auto, cantidad, precio_unitario) VALUES
    (2, 2, 2, 1, 280000.00);

    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (5, 'Ferrari 812 Superfast', 'Coupé de lujo con motor V12 de 800 hp', 350000.00, 4);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (6, 'Ferrari F8 Tributo', 'Deportivo con motor V8 biturbo de 710 hp', 300000.00, 6);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (7, 'Ferrari Portofino M', 'Cabrio con motor V8 biturbo de 620 hp', 230000.00, 5);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (8, 'Ferrari LaFerrari', 'Híbrido con motor V12 y eléctrico de 950 hp', 1500000.00, 2);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (9, 'Ferrari GTC4Lusso', 'Coupé de lujo con motor V12 de 680 hp', 350000.00, 3);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (10, 'Ferrari California T', 'Convertible con motor V8 biturbo de 560 hp', 220000.00, 4);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (11, 'Ferrari 488 Pista', 'Deportivo con motor V8 biturbo de 710 hp', 350000.00, 3);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (12, 'Ferrari F12 Berlinetta', 'Coupé con motor V12 de 740 hp', 320000.00, 4);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (13, 'Ferrari Monza SP2', 'Edición limitada con motor V12 de 810 hp', 1200000.00, 2);
    
    INSERT INTO Autos (id_auto, modelo, descripcion, precio, stock) VALUES
    (14, 'Ferrari 246 Dino', 'Clásico deportivo con motor V6 de 180 hp', 250000.00, 5);


END;
