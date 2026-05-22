# tareas.py · Seguimiento del proyecto
# Proyecto: LevelUp Gym

pendientes = [
    # Agregá las tareas que tienen pendientes
    "Conectar frontend con backend",
    "Integrar sistema de seguimiento de progreso físico",
    "Agregar carrito de compras para productos fitness",
    "Implementar pasarela de pagos para suplementos y accesorios"
]

completadas = [
    # Agregá lo que ya terminaron
    "Diseño inicial de la interfaz de usuario",
    "Definición de funcionalidades principales del sistema",
    "Diseño de base de datos",
    "Creación de estructura del proyecto",
]

en_progreso = [
    # Lo que están haciendo ahora mismo
    "Diseño de pantallas de rutinas y progreso",
    "Desarrollo del módulo de rutinas personalizadas",
    "Carga de productos fitness en la tienda virtual",
]

print("=" * 40)
print("SEGUIMIENTO DEL PROYECTO")
print("=" * 40)

print("\n📌 DESCRIPCIÓN DEL PROYECTO:")
print("Con LevelUp Gym, buscamos digitalizar y modernizar la experiencia del gimnasio,")
print("conectando a los usuarios con rutinas efectivas y progresivas.")
print("Los usuarios podrán llevar un seguimiento digitalizado de su progreso físico.")
print("Además, se comercializarán productos como straps, cinturones y suplementos")
print("fitness para complementar la experiencia.")

print("\n✅ COMPLETADAS:")
for t in completadas:
    print(f"   ✅ {t}")

print("\n🔧 EN PROGRESO:")
for t in en_progreso:
    print(f"   🔧 {t}")

print("\n⬜ PENDIENTES:")
for t in pendientes:
    print(f"   ⬜ {t}")

print("\n" + "=" * 40)
print(f"Total tareas: {len(completadas) + len(en_progreso) + len(pendientes)}")
print(f"Completadas:  {len(completadas)}")
print(f"Pendientes:   {len(pendientes)}")