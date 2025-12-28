#!/usr/bin/env python3
"""
FastAPI Backend Server for Physical Menu to Website Converter
Provides API endpoints for processing menu images and extracting colors.
"""

import argparse
import sys
import os
from pathlib import Path
from typing import List

# Add current directory to path to import local modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from fastapi import FastAPI, HTTPException
    from fastapi.middleware.cors import CORSMiddleware
    from pydantic import BaseModel
    import uvicorn
except ImportError:
    print("Error: FastAPI and uvicorn are required. Install with: pip install fastapi uvicorn", file=sys.stderr)
    sys.exit(1)

from smart_menu import SmartMenu
from smart_color import SmartColor

app = FastAPI(title="Menu Processor API", version="1.0.0")

# Enable CORS for Electron app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImagePathsRequest(BaseModel):
    """Request model for image processing endpoints."""
    image_paths: List[str]


@app.get("/")
async def root():
    """Health check endpoint."""
    return {"status": "running", "service": "Menu Processor API"}


@app.post("/process-images")
async def process_images(request: ImagePathsRequest):
    """
    Process menu images to extract text content.
    
    Args:
        request: ImagePathsRequest containing list of image file paths
        
    Returns:
        Dictionary with extracted text content from images
    """
    try:
        image_paths = request.image_paths
        
        # Validate that all image paths exist
        for path in image_paths:
            if not os.path.exists(path):
                raise HTTPException(status_code=404, detail=f"Image not found: {path}")
        
        # Process images using SmartMenu
        sm = SmartMenu(image_paths)
        result = sm.get_html_body()
        
        return {
            "success": True,
            "data": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/extract-colors")
async def extract_colors(request: ImagePathsRequest):
    """
    Extract prominent colors from menu images.
    
    Args:
        request: ImagePathsRequest containing list of image file paths
        
    Returns:
        Dictionary with extracted colors from images
    """
    try:
        image_paths = request.image_paths
        
        # Validate that all image paths exist
        for path in image_paths:
            if not os.path.exists(path):
                raise HTTPException(status_code=404, detail=f"Image not found: {path}")
        
        # Extract colors using SmartColor
        sc = SmartColor(image_paths, colors=4)
        colors = sc.global_colors()
        
        return {
            "success": True,
            "colors": colors
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def main():
    """Main entry point for the FastAPI server."""
    parser = argparse.ArgumentParser(description="FastAPI Backend Server for Menu Processing")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the server on (default: 8000)")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to bind to (default: 127.0.0.1)")
    
    args = parser.parse_args()
    
    print(f"Starting FastAPI server on {args.host}:{args.port}", flush=True)
    
    uvicorn.run(
        app,
        host=args.host,
        port=args.port,
        log_level="info"
    )


if __name__ == "__main__":
    main()
