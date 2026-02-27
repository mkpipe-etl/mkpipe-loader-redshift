from mkpipe.spark import JdbcLoader


class RedshiftLoader(JdbcLoader, variant='redshift'):
    driver_name = 'redshift'
    driver_jdbc = 'com.amazon.redshift.jdbc42.Driver'

    def build_jdbc_url(self):
        url = (
            f'jdbc:{self.driver_name}://{self.host}:{self.port}/{self.database}'
            f'?user={self.username}&password={self.password}'
        )
        if self.schema:
            url += f'&currentSchema={self.schema}'
        return url
