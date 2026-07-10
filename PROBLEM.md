# Urban Air Quality and Climate Pattern Analysis

## Overview

This project is a hands-on capstone exercise designed to consolidate the core concepts taught in Chapter 5 of *Python for Data Analysis*: pandas' fundamental data structures (`Series` and `DataFrame`), intrinsic data alignment through Index objects, missing-data handling, label- and position-based indexing (`loc` / `iloc`), and descriptive statistics.

Rather than working with a clean, ready-made dataset, the project is deliberately built around **messy, inconsistent, real-world-like data**. The goal is not to demonstrate pandas syntax in isolation, but to force an authentic analytical workflow: ingesting raw nested data, building proper tabular structures from it, reconciling mismatched sources, diagnosing data quality issues, and summarizing findings numerically. This mirrors what a data analyst actually encounters in practice, where sensors fail, systems don't share a common schedule, and data arrives in raw, unaligned formats.

## Why This Project Matters

Learning pandas from documentation examples alone tends to produce shallow familiarity: a person can recognize `df.loc[...]` or `df.isna()` without understanding *why* those tools exist or *when* to reach for them. This project addresses that gap by embedding each pandas concept inside a problem that only makes sense to solve with that concept:

- Data arrives as **nested Python dictionaries**, so building DataFrames from dictionaries becomes a necessity, not an exercise.
- Two data sources are recorded on **different schedules**, so pandas' automatic index alignment becomes the natural (and only sensible) way to merge them.
- Some data is **entirely absent** for stretches of time, and some sources are **structurally incomplete** (missing an entire city), so missing-data detection and handling become required steps rather than optional add-ons.
- Answering the project's business questions requires **slicing by date ranges and by city**, so `loc` and `iloc` are used purposefully rather than for their own sake.
- Determining which city experienced the most extreme conditions requires **descriptive statistics**, tying the whole exercise back to summarization.

In short, the project is structured so that mastering pandas is the *means* of solving a concrete problem, not the end goal in itself.

## Formal Problem Definition

**Context:** An environmental agency has collected data from two independent sensor networks across several cities over the course of one month.

- **Network A** measures airborne particulate matter (PM2.5) and general air quality.
- **Network B** measures temperature and humidity.

**The Problem:** The two networks operate independently and have known operational flaws:

1. Their recording dates and times do not line up perfectly (index mismatch between sources).
2. Some cities' sensors failed for several consecutive days, producing missing readings.
3. The raw data arrives in nested, unprocessed formats (raw Python dictionaries / JSON), rather than as clean tables.

**Objective:** Build a script that ingests these raw nested structures, converts them into proper pandas data structures, aligns the measurements by their temporal and geographic indices, diagnoses the health of the data (identifying gaps and their extent), and produces a descriptive statistical report to determine which city experienced the most extreme environmental conditions during the observed period.

## Building the Synthetic Dataset

To make the exercise realistic, the dataset is **not** generated using pandas. Instead, it is built using plain Python (dictionaries, lists, and the `random` module) to simulate consuming raw data from an external API or a legacy system — exactly the kind of input a real analyst would receive before any cleaning takes place.

### Data Design

The dataset simulates three cities — Madrid, Bogotá, and Mexico City (CDMX) — over a full month (January 2024, 31 days).

- **Network A (PM2.5):** a two-level structure of *city → date → value*, recorded daily for every city.
- **Network B (Temperature / Humidity):** a three-level structure of *city → date → {temperature, humidity}*, recorded only on weekdays.

### Intentional Inconsistencies

Three categories of imperfection are deliberately injected so that each core pandas skill has a genuine reason to be used:

1. **Index Mismatch:** Network A records every single day, while Network B — due to a configuration limitation — does not record readings on weekends. When the two networks are combined, pandas must reconcile dates that exist in one source but not the other.
2. **Native Missing Values:** The PM2.5 sensor in Bogotá is simulated to have failed for a six-day stretch in the middle of the month. Those readings are recorded as null values, which pandas will interpret as `NaN` once loaded.
3. **Structural Missingness:** Network B has no entry at all for Madrid, simulating a delay in that city's climate-sensor installation — an entire key is absent rather than individual values within it.

### Persisting the Data

To reinforce a realistic workflow, the generated dictionaries are not passed directly into pandas in memory. Instead, they are **persisted to disk as JSON files** — one for each network — before any analysis begins. This adds a necessary "step zero" to the exercise: reading raw files from disk, rather than working with data that is already conveniently available as Python objects.

The Network B file is particularly instructive, since it is a dictionary nested three levels deep (city → date → metric), which requires deliberate thought about how to flatten it into a proper two-dimensional DataFrame structure once it is loaded.

## Deliverables

By the end of the project, the following should be produced:

- A synthetic, intentionally inconsistent dataset for both sensor networks, persisted as JSON files.
- A pandas-based ingestion and cleaning pipeline that loads, aligns, and audits the data.
- A missing-data diagnostic summarizing how many readings were lost, broken down by city and by network.
- A composite "risk index" combining air quality and climate metrics, correctly handling misaligned dates.
- A descriptive statistical report identifying which city experienced the most extreme environmental conditions during the period studied.
