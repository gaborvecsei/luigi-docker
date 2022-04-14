from pathlib import Path
import random
import time
from typing import List

import luigi


class BananaProcessor(luigi.Task):
    banana_number = luigi.IntParameter()
    folder_path = luigi.Parameter()

    def run(self):
        # Randomly wait to simulate long running task
        rnd_wait_time: float = random.uniform(0, 3)
        time.sleep(rnd_wait_time)

        text = "\n".join(["banana"] * int(self.banana_number))
        with open(self.output().path, "w") as outfile:
            outfile.write(text)

    def output(self):
        file_path = Path(self.folder_path) / f"banana_{self.banana_number}.txt"
        file_path = str(file_path)
        return luigi.LocalTarget(file_path)


class BananaAggregator(luigi.Task):
    nb_banana_tasks = luigi.IntParameter(default=10)
    output_folder_path = luigi.Parameter(default="/tmp/luigi_test")
    output_file_name = luigi.Parameter(default="banana_agg.txt")

    def output(self):
        output_file_path: Path = Path(str(self.output_folder_path)) / str(self.output_file_name)
        return luigi.LocalTarget(output_file_path)

    def requires(self):
        tasks = [
            BananaProcessor(banana_number=x, folder_path=str(self.output_folder_path))
            for x in range(self.nb_banana_tasks)
        ]

        return tasks

    def run(self):
        agg_text: List[str] = []

        # Concat the content of the files
        for b in self.input():
            with b.open("r") as input_file:
                agg_text.append(input_file.read())
                agg_text.append("-" * 30)

        text = "\n".join(agg_text)
        with open(self.output().path, "w") as outfile:
            outfile.write(text)


class RootOfAllBananas(luigi.Task):

    def requires(self):
        return BananaAggregator(output_folder_path="/tmp/luigi_test",
                                output_file_name="banana_agg.txt",
                                nb_banana_tasks=10)
