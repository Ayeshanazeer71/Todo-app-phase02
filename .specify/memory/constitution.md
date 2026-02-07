<!--
Sync Impact Report:
- Version change: 1.0.0 → 2.0.0 (major update - new external dependencies and modular structure)
- Modified principles: VI. Pure Standard Library Dependencies → VI. Rich Library for Console UI
- Added sections: VII. Modular Project Structure
- Templates requiring updates: ⚠ pending - plan-template.md, spec-template.md, tasks-template.md
- Follow-up TODOs: Update all templates to reflect new principles
-->
# Todo Console App Constitution

## Core Principles

### I. Python 3.13+ with Strict Type Hints and Documentation
All code must use Python 3.13+ with mandatory type hints on all function signatures, class attributes, and complex variable assignments. Code must include Google-style docstrings for all functions, classes, and modules. This ensures code clarity, prevents type-related bugs, enables better IDE support and static analysis, and provides comprehensive documentation. Rationale: Type safety, maintainability, and documentation are critical for long-term code health.

### II. In-Memory Storage Only
The application must use only in-memory storage (Python lists/dicts) with no external databases, files, or persistence mechanisms. All data exists only during runtime and is lost when the program terminates. Rationale: Simplicity and focus on core functionality without the complexity of persistence layers.

### III. Clean Task Model
Each task must follow the defined model: id (auto-incrementing integer), title (string), description (string), and completed (boolean with default False). The model is immutable except through explicit update operations. Rationale: Consistent data structure ensures predictable behavior and simplifies implementation.

### IV. Beautiful Console Experience with Rich Library
The application must use the 'rich' library for rich text, tables, panels, colors, and emojis in console. This creates a beautiful, intuitive console experience with enhanced visual appeal. Rationale: Professional appearance and improved user experience through rich formatting capabilities.

### V. Comprehensive Input Validation and Error Handling
All potential error conditions must be handled gracefully with user-friendly error messages: invalid task IDs, empty task lists, malformed input, and other edge cases. The application should never crash due to user input or expected error conditions. All user inputs must be validated comprehensively. Rationale: Robustness, good user experience, and input safety.

### VI. Rich Library for Console UI
The application must use the 'rich' library as an external dependency for all console UI elements including tables, panels, colors, and emojis. This replaces the pure standard library requirement for UI components. Rationale: Enhanced visual experience and professional appearance that meets modern console application standards.

### VII. Modular Project Structure
The codebase must follow a clean separation of concerns with the following modular structure under `/src`:
- `models.py` → Task dataclass and other data models
- `operations.py` → All CRUD functions (add, list, update, delete, toggle status)
- `ui.py` → All display, menu, prompts, and rich formatting
- `main.py` → Entry point with menu loop only
This ensures clean separation of concerns and maintainable code organization. Rationale: Maintainable, testable, and organized codebase with clear functional boundaries.

## Project Structure
The codebase must follow the specified modular structure with all source code located in the `/src` directory, containing the four required modules as specified in Principle VII. All functionality should be logically organized according to the separation of concerns principle. Rationale: Maintainable and organized codebase with clear functional boundaries.

## Development Workflow
All development must follow spec-driven development principles where no manual coding occurs without proper specifications first. Features must be planned, specified, and tasked before implementation. The development cycle focuses on the five basic features required for Phase I: Add, List/View, Update, Delete, and Mark Complete. Rationale: Ensures systematic development and prevents scope creep.

## Governance

This constitution governs all development of the Todo Console App. All code changes must comply with these principles. Amendments to this constitution require explicit documentation of the change, its rationale, and approval before implementation. Versioning follows semantic versioning where major changes break compatibility with previous principles, minor changes add new principles, and patches clarify existing principles.

**Version**: 2.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
