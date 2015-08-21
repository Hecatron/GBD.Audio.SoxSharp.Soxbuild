add_library(gsm add code decode gsm_create gsm_decode gsm_destroy gsm_encode gsm_option long_term lpc preprocess rpe short_term table)

# Set the Output Directory for libs
set_target_properties( gsm
    PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/../../LibOutput"
)
