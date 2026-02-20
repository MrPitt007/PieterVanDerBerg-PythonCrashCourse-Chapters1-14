

def print_models(unprinted_designs, completed_models):
    """Move designs from 'unprinted_designs' to 'completed_models'."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Display the models that have been printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f"- {model}")


 Demo run (as if main program imported these from printing_functions.py)
_unprinted = ['phone case', 'robot pendant', 'dodecahedron']
_completed = []
print_models(_unprinted[:], _completed)     # use a copy so original remains
show_completed_models(_completed)




 Simulate: import printing_functions as a namespace object.
class _ModuleSim:
    print_models = staticmethod(print_models)
    show_completed_models = staticmethod(show_completed_models)

printing_functions = _ModuleSim()  # acts like: import printing_functions

# Use "module_name.function()"
_unprinted = ['cube', 'pyramid']
_completed = []
printing_functions.print_models(_unprinted[:], _completed)
printing_functions.show_completed_models(_completed)


# ---------- 2) from module_name import function_name ----------
# Bind direct names as if imported specifically
print_models_imported = print_models
show_completed_models_imported = show_completed_models

_unprinted = ['gear', 'hinge']
_completed = []
print_models_imported(_unprinted[:], _completed)
show_completed_models_imported(_completed)


# ---------- 3) from module_name import function_name as fn ----------
pm = print_models          # alias for brevity (like: ... as pm)
scm = show_completed_models

_unprinted = ['sphere']
_completed = []
pm(_unprinted[:], _completed)
scm(_completed)


# ---------- 4) import module_name as mn ----------
pf = printing_functions    # alias to the simulated module namespace
_unprinted = ['torus', 'bracket']
_completed = []
pf.print_models(_unprinted[:], _completed)
pf.show_completed_models(_completed)


# ---------- 5) from module_name import * ----------
# Wildcard import would place all public names into the current namespace.
# It's generally discouraged because it obscures where names come from and
# can cause collisions. We avoid demonstrating it in code intentionally.
print("\n[Note] Avoid: from module_name import *  (namespace pollution)")


# ==================================================
# 8-17 — STYLING FUNCTIONS (apply guidelines to 3 functions)
# --------------------------------------------------
# The page asks you to ensure three of your programs follow the styling rules.
# Below are clean, PEP 8–friendly examples with docstrings, defaults,
# keyword-argument spacing, and line-length wrapping.

def make_sandwich(*items):
    """Return a human-readable summary of a sandwich order."""
    if not items:
        return "Sandwich with (no specified items)."
    listed = ", ".join(items)
    return f"Sandwich with: {listed}."


def create_user_profile(first_name, last_name, **extra):
    """
    Return a user profile dictionary.

    Required:
        first_name (str)
        last_name  (str)
    Optional (**extra):
        Arbitrary named fields (e.g., role, location).
    """
    profile = {'first_name': first_name, 'last_name': last_name}
    profile.update(extra)
    return profile


def generate_report(
    title,
    author,
    created_at,
    section_1,
    section_2,
    section_3,
    footer_note="All values provisional.",
):
    """Return a text report; signature wrapped for readability."""
    parts = [
        f"# {title}",
        f"Author: {author} — {created_at}",
        "",
        section_1,
        "",
        section_2,
        "",
        section_3,
        "",
        f"Note: {footer_note}",
    ]
    return "\n".join(parts)


# Quick checks showing calls with keyword args (no spaces around '='):
print("\nStyled examples:")
print(make_sandwich('lettuce', 'tomato', 'hummus'))
print(create_user_profile('Pieter', 'Van Der Berg', role='applikationsutvecklare',
                          location='Övertorneå'))
print(generate_report(
    title="Chapter 8 QA",
    author="Pieter",
    created_at="2026-02-20",
    section_1="• Functions and arguments reviewed",
    section_2="• Modules and imports verified",
    section_3="• Styling applied",
))


# ==================================================
# CHAPTER 8 — SUMMARY (from the page’s closing section)
# --------------------------------------------------

chapter_summary = """
CHAPTER 8 SUMMARY
-----------------
• You learned to write functions and pass information via parameters.
• You used positional, keyword, default, and arbitrary arguments (*args/**kwargs).
• You wrote functions that print results and functions that return values.
• You practiced functions with lists, dictionaries, if statements, and while loops.
• You organized code by placing functions in separate modules and importing them.
• You followed styling conventions so programs remain readable and well-structured.

Big takeaway: build small, focused functions; call them where needed. When you
change a function, the improvement applies everywhere that function is used.
"""
print(chapter_summary)
