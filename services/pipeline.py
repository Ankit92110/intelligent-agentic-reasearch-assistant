"""
Application startup pipeline.

This module prepares everything needed
before the interactive chat loop begins.
"""

import sys

from services.index_manager import IndexManager

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001, S110
        pass


def initialize_pipeline() -> IndexManager:
    """
    Initialize the RAG pipeline.

    Workflow:

        1. Discover available document collections.
        2. Initialize the index manager.

    Returns:
        An initialized IndexManager instance.
    """

    print("📂 Discovering document collections...")

    index_manager = IndexManager()

    if not index_manager.list_collections():
        print("⚠️ No document collections found.")

    print("✅ Pipeline initialized.\n")

    return index_manager
