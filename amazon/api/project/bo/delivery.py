from amazon.api.project.utils import Graph, objLogger


def amazon_delivery(req_data):
    start = req_data["start"]
    checkpoint = req_data["checkpoint"]
    finish = req_data["finish"]
    objLogger.info(f"Start: {start}\tCheckpoint: {checkpoint}\tFinish: {finish}")
    graph = Graph()

    path_to_checkpoint, distance_to_checkpoint = graph.dijkstra(start, checkpoint)

    path_to_finish, distance_to_finish = graph.dijkstra(checkpoint, finish)

    total_path = path_to_checkpoint + path_to_finish[1:]
    total_distance = distance_to_checkpoint + distance_to_finish
    objLogger.info(f"Distance: {total_distance}\tPath: {', '.join(total_path)}")

    return {"steps": total_path, "distance": total_distance}
