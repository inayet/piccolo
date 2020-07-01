import datetime
import decimal
from unittest import TestCase
import uuid

from piccolo.columns.column_types import (
    BigInt,
    Date,
    DateDefault,
    ForeignKey,
    Integer,
    Numeric,
    Real,
    SmallInt,
    Text,
    Time,
    TimeDefault,
    Timestamp,
    TimestampDefault,
    UUID,
    UUIDDefault,
    Varchar,
)
from piccolo.table import Table


class TestDefaults(TestCase):
    """
    Columns check the type of the default argument.
    """

    def test_int(self):
        for _type in (Integer, BigInt, SmallInt):
            _type(default=0)
            _type(default=None, null=True)
            with self.assertRaises(ValueError):
                _type(default="hello world")
            with self.assertRaises(ValueError):
                _type(default=None, null=False)

    def test_text(self):
        for _type in (Text, Varchar):
            _type(default="")
            _type(default=None, null=True)
            with self.assertRaises(ValueError):
                _type(default=123)
            with self.assertRaises(ValueError):
                _type(default=None, null=False)

    def test_real(self):
        Real(default=0.0)
        Real(default=None, null=True)
        with self.assertRaises(ValueError):
            Real(default="hello world")
        with self.assertRaises(ValueError):
            Real(default=None, null=False)

    def test_numeric(self):
        Numeric(default=decimal.Decimal(1.0))
        Numeric(default=None, null=True)
        with self.assertRaises(ValueError):
            Numeric(default="hello world")
        with self.assertRaises(ValueError):
            Numeric(default=None, null=False)

    def test_uuid(self):
        UUID(default=None, null=True)
        UUID(default=UUIDDefault.uuid4)
        UUID(default=uuid.uuid4())
        with self.assertRaises(ValueError):
            UUID(default="hello world")
        with self.assertRaises(ValueError):
            UUID(default=None, null=False)

    def test_time(self):
        Time(default=None, null=True)
        Time(default=TimeDefault.now)
        Time(default=datetime.datetime.now().time())
        with self.assertRaises(ValueError):
            Time(default="hello world")
        with self.assertRaises(ValueError):
            Time(default=None, null=False)

    def test_date(self):
        Date(default=None, null=True)
        Date(default=DateDefault.now)
        Date(default=datetime.datetime.now().date())
        with self.assertRaises(ValueError):
            Date(default="hello world")
        with self.assertRaises(ValueError):
            Date(default=None, null=False)

    def test_timestamp(self):
        Timestamp(default=None, null=True)
        Timestamp(default=TimestampDefault.now)
        Timestamp(default=datetime.datetime.now())
        with self.assertRaises(ValueError):
            Timestamp(default="hello world")
        with self.assertRaises(ValueError):
            Timestamp(default=None, null=False)

    def test_foreignkey(self):
        ForeignKey(references=Table(), default=None, null=True)
        ForeignKey(references=Table(), default=1)
        with self.assertRaises(ValueError):
            ForeignKey(references=Table, default="hello world")
        with self.assertRaises(ValueError):
            ForeignKey(references=Table, default=None, null=False)
