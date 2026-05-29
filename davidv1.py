# info-proyecto.py
# Completa este archivo con los datos reales de tu proyecto
# Ejecutalo con: python info-proyecto.py

# ── DATOS DEL PROYECTO ──────────────────────────────────────
nombre_proyecto = "LevelUp Gym"

descripcion = (
    "LevelUp Gym busca digitalizar y modernizar la experiencia "
    "del gimnasio mediante rutinas personalizadas, seguimiento "
    "del progreso físico y una tienda virtual de productos fitness."
)

tecnologias = [
    "C# .NET",
    "Angular Js",
    "MySQL"
]

integrantes = [
    "David Gonzalez",
    "Brayan Valencia",
    "Hillary Cordoba Ocoro"
]

funcionalidades = [
    "Login y registro de usuarios",
    "Rutinas personalizadas",
    "Seguimiento de progreso físico",
    "Tienda virtual fitness",
    "Carrito de compras",
    "Pasarela de pagos",
    "Panel administrativo"
]

estado = "En construccion"

# ── TAREAS DEL EQUIPO ────────────────────────────────────────
tareas_completadas = [
    "Diseño inicial de la interfaz de usuario",
    "Definición de funcionalidades principales del sistema",
    "Diseño de base de datos",
    "Creación de estructura del proyecto"
]

tareas_pendientes = [
    "Conectar frontend con backend",
    "Integrar sistema de seguimiento de progreso físico",
    "Agregar carrito de compras para productos fitness",
    "Implementar pasarela de pagos para suplementos y accesorios"
]

tareas_en_progreso = [
    "Diseño de pantallas de rutinas y progreso",
    "Desarrollo del módulo de rutinas personalizadas",
    "Carga de productos fitness en la tienda virtual"
]

# ── FUNCIONES ────────────────────────────────────────────────
def mostrar_info():
    print("=" * 45)
    print(f"  PROYECTO: {nombre_proyecto}")
    print("=" * 45)
    print(f"  Descripcion : {descripcion}")
    print(f"  Estado      : {estado}")
    print(f"  Tecnologias : {', '.join(tecnologias)}")
    print(f"  Integrantes : {', '.join(integrantes)}")

def mostrar_funcionalidades():
    print("\n  FUNCIONALIDADES:")
    for i, f in enumerate(funcionalidades, 1):
        print(f"    {i}. {f}")

def mostrar_tareas():
    print("\n  TAREAS COMPLETADAS:")
    for t in tareas_completadas:
        print(f"    [x] {t}")

    print("\n  EN PROGRESO:")
    for t in tareas_en_progreso:
        print(f"    [~] {t}")

    print("\n  PENDIENTES:")
    for t in tareas_pendientes:
        print(f"    [ ] {t}")

    total = (
        len(tareas_completadas)
        + len(tareas_pendientes)
        + len(tareas_en_progreso)
    )

    print(f"\n  Total tareas: {total} | Completadas: {len(tareas_completadas)}")

# ── EJECUTAR ─────────────────────────────────────────────────
mostrar_info()
mostrar_funcionalidades()
mostrar_tareas()

print("\n" + "=" * 45)