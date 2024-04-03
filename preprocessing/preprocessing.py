import pandas as pd

class Preprocessing():
    def __init__(self, dataframe, minutes_gap=30, min_records_in_session=1):
        self.dataframe = dataframe
        self.minutes_gap = minutes_gap
        self.min_records_in_session = min_records_in_session

        self.split_dataframe()
        self.create_session_dataframe()
        self.split_last_value()

    def split_sessions(self, group, minutes_gap=30):
        max_gap = pd.Timedelta(minutes=minutes_gap)
        group = group.sort_values('timestamp')
        diffs = group['timestamp'].diff()
        session_starts = diffs > max_gap
        group['session_id'] = session_starts.cumsum()
        return group
    

    def split_dataframe(self):
        self.dataframe['timestamp'] = pd.to_datetime(self.dataframe['timestamp'])
        self.dataframe = self.dataframe.sort_values(by=['user', 'timestamp'])

        # Aplica a função split_sessions a cada grupo de usuários
        self.dataframe = self.dataframe.groupby('user').apply(lambda group: self.split_sessions(group, self.minutes_gap)).reset_index(drop=True)

        # Ajusta o session_id para ser único em todo o DataFrame
        self.dataframe['global_session_id'] = self.dataframe['user'].astype(str) + '_' + self.dataframe['session_id'].astype(str)
        return self.dataframe
    
    def create_session_dataframe(self):
        session_df = self.dataframe.groupby('global_session_id')['song'].agg(list).reset_index()
        self.session_df = session_df[session_df['song'].apply(lambda x: len(x) >= self.min_records_in_session)]
    
    def _split_last_value(self, lst):
        return lst[:-1], lst[-1]
    
    def split_last_value(self):
        self.session_df[['song_list', 'last_song']] = self.session_df['song'].apply(lambda x: pd.Series(self._split_last_value(x)))