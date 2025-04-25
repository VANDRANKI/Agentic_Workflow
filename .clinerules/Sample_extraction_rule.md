## Mandatory Rule

1. Sample extraction rule, you need to identify the all the samples in the research article, in which the research article is about testing ceria abrasives on silicon dioxide and silicon nitride Chemical Mechanical Planarization (CMP).

2. The research article will be given in the markdown format, and where images are included, the image address is given to the relevant file of the image, which should be uploaded to the model to read to get the get all the information that is required for the sample extraction. 

3. The model must read the entire paper and it's images to fully grash the information for all the samples discussed in the research ariticle, it can be 1 sample, 2 samples, or as many as 20 samples in one reserach article. 

4. Each sample should have it's own .JSON File, if the number of samples identified is 1 the output can be just 1, but if the number of samples are 20 then the output will be 20 JSON files. 

5. Each sample should have it's unique and accurate information for the following attributes: Each Should be named DOI_Unique_Sample_ID.

6. If the values are not available in the markdown file, the model should be able to read the values from the image files of that particular research article, using it's tools by using the image path.

{
  "description": "Sample entry with full experimental details. All fields can be populated independently for each unique experimental sample.",

  "doi": "",

  "sample_id": "",

  "experiment_context": "",

  "abrasive_synthesis": {
    "description": "Abrasive synthesis details: includes precursors, synthesis parameters (chemical & physical), and post-synthesis treatments, excludes slurry formulation additives. Note: Additional precursors can be added following the same structure.",

    "precursors": [
      {
        "material_name": "",

        "formula": "",

        "source_type": "",

        "purity": "",

        "quantity": {
          "value": "",

          "unit": ""
        }
      }
    ],

    "synthesis_parameters": {
      "chemical": {
        "description": "Chemical parameters: solvents, pH agents, and synthesis additives. Note: Additional solvents can be added following the same structure.",

        "solvents": [
          {
            "name": "",

            "quantity": {
              "value": "",

              "unit": ""
            }
          }
        ],

        "ph_agents": [
          {
            "name": "",

            "concentration": {
              "value": "",

              "unit": ""
            }
          }
        ],

        "synthesis_additives": []
      },

      "physical": {
        "description": "Physical process sequences can be from these process in any possible other Calcination, milling, seperation, hydrothermal, centrigure, filtration, mixing, washing etc. Note: Additional process stages can be added in proper sequence following the same structure.",

        "process_stages": [
          {
            "stage": 1,

            "value": "",

            "unit": "",

            "duration": {
              "value": "",

              "unit": ""
            }
          }
        ]
      }
    },

    "post_synthesis": {
      "description": "Post-synthesis procedures: collection methods and treatment processes.",

      "collection": {
        "method": "",

        "parameters": {
          "speed": {
            "value": "",

            "unit": ""
          },

          "cycles": "",

          "wash_volume": {
            "value": "",

            "unit": ""
          }
        }
      },

      "treatment": {
        "calcination": {
          "temperature": {
            "value": "",

            "unit": ""
          },

          "duration": {
            "value": "",

            "unit": ""
          }
        }
      }
    }
  },

  "slurry_preparation": {
    "description": "Slurry preparation details: composition and processing steps, includes only chemical after the abrasives is synthesized and does't include previously added additives.",

    "composition": {
      "abrasive": {
        "material": "",

        "concentration": {
          "initial": "",

          "final": "",

          "unit": ""
        }
      },

      "slurry_additives": [
        {
          "name": "",

          "type": "",

          "concentration": {
            "value": "",

            "unit": ""
          }
        }
      ],

      "solvent": {
        "name": "",

        "percentage": {
          "value": "",

          "unit": ""
        }
      }
    },

    "processing": {
      "description": "Processing parameters: dispersion methods, stabilization processes, and pH control.",

      "dispersion": [],

      "stabilization": {
        "aging": {
          "duration": {
            "value": "",

            "unit": ""
          },

          "equipment": ""
        }
      },

      "ph_control": {
        "target": {
          "min": "",

          "max": ""
        },

        "agents": [
          {
            "name": "",

            "concentration": {
              "value": "",

              "unit": ""
            }
          }
        ]
      }
    }
  },

  "characterization": {
    "description": "Slurry characterization details: abrasive morphology, crystallinity, etc",

    "morphology": {
      "particle_size": {
        "average": {
          "min": "",

          "max": "",

          "unit": ""
        }
      },

      "shape": "",

      "surface_area": {
        "value": "",

        "unit": ""
      }
    },

    "stability": ""
  }
}
