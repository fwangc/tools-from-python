import gpxpy
import gpxpy.gpx
from tcxparser import TCXParser

def convert_tcx_to_gpx(tcx_file_path, gpx_file_path):
    parser = TCXParser(tcx_file_path)
    gpx = gpxpy.gpx.GPX()

    for track in parser.tracks:
        gpx_track = gpxpy.gpx.GPXTrack()
        gpx.tracks.append(gpx_track)

        gpx_segment = gpxpy.gpx.GPXTrackSegment()
        gpx_track.segments.append(gpx_segment)

        for point in track.points:
            gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(point.latitude, point.longitude, point.time))

    with open(gpx_file_path, 'w') as gpx_file:
        gpx_file.write(gpx.to_xml())

# Example usage:
convert_tcx_to_gpx('geo_file.tcx', 'geo_file.gpx')