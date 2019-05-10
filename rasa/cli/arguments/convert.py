def add_arguments(parser):
    parser.add_argument(
        "-d", "--data_file", required=True, help="file or dir containing training data"
    )

    parser.add_argument(
        "-o",
        "--out_file",
        required=True,
        help="file where to save training data in rasa format",
    )

    parser.add_argument("-l", "--language", default="en", help="language of the data")
